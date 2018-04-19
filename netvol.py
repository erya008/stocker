#!/usr/bin/env python
# coding=utf8
from dateutil import parser
import time
import sys
from datetime import datetime
from itertools import islice  

def t_to_str(t):
    return datetime.fromtimestamp(t).strftime('%Y-%m-%dT%H:%M:00')

class Global(object):
    NON = 0
    LONG = 1
    OPEN_PRICE = 0
    OPEN_MIN = 0
    SHORT = 2
    TOTAL = 1

header = ['match_id', 'timestamp', 'price', 'side', 'vol']


class Backtest(object):
    def __init__(self, tick_file):
        self.tick_file = tick_file
        self.status = Global.NON

        self.k = []

    def run(self):
        for line in islice(file(self.tick_file),1,None):
            line = line.strip().split(',')
            data = dict(zip(header, line))
            data['price'] = float(data['price'])
            
            data['vol'] = int(data['vol'])
            data['minute'] = int(time.mktime(parser.parse(data['timestamp']).timetuple()))
            data['minute'] = data['minute'] / 60
            self.on_ticker(data)

    def data_to_k(self, data):
        return {
            'open': data['price'],
            'close': data['price'],
            'low': data['price'],
            'high': data['price'],
            'buy_vol': data['vol'] if data['side'] == 'Buy' else 0,
            'sell_vol': data['vol'] if data['side'] == 'Sell' else 0,
            'vol': data['vol'],
            'minute': data['minute'],
            'timestamp': data['timestamp']
        }

    def on_ticker(self, data):
        if not self.k or data['minute'] != self.k[-1]['minute']:
            if self.k:
                last_k = self.k[-1]
                self.on_k(last_k)
                for x in range(self.k[-1]['minute'] + 1, data['minute']):
                    self.k.append({
                        'open': last_k['close'],
                        'close': last_k['close'],
                        'low': last_k['close'],
                        'high': last_k['close'],
                        'buy_vol': 0,
                        'sell_vol': 0,
                        'vol': 0,
                        'minute': x,
                        'timestamp': last_k['timestamp']
                    })
                    self.on_k(self.k[-1])

            new_k = self.data_to_k(data)
            self.k.append(new_k)
        else:
            last_k = self.k[-1]
            last_k['low'] = min(last_k['low'], data['price'])
            last_k['high'] = max(last_k['high'], data['price'])
            last_k['buy_vol'] += data['vol'] if data['side'] == 'Buy' else 0
            last_k['sell_vol'] += data['vol'] if data['side'] == 'Sell' else 0
            last_k['vol'] += data['vol']

        if len(self.k) > 10000:
            self.k = self.k[-1000:]

    def on_k(self, k):
        if len(self.k) < 10:
            return

        if self.status == Global.LONG and not Global.OPEN_PRICE:
            Global.OPEN_PRICE = k['low']
            Global.OPEN_MIN = k['minute']
            return
        if self.status == Global.SHORT and not Global.OPEN_PRICE:
            Global.OPEN_PRICE = k['high']
            Global.OPEN_MIN = k['minute']
            return

        if self.status == Global.LONG and Global.OPEN_PRICE and k['minute'] >= Global.OPEN_MIN + 2:
            diff = (k['low'] - Global.OPEN_PRICE) / Global.OPEN_PRICE - 0.001
            Global.TOTAL *= 1 + diff
            print( '%s LONG: %.1f - %.2f = %.2f%%, value: %.2f' % (t_to_str(Global.OPEN_MIN * 60), k['low'], Global.OPEN_PRICE, diff * 100, Global.TOTAL))
            self.status = Global.NON
            Global.OPEN_PRICE = 0
            Global.OPEN_MIN = 0
            return

        if self.status == Global.SHORT and Global.OPEN_PRICE and k['minute'] >= Global.OPEN_MIN + 2:
            diff = (Global.OPEN_PRICE - k['high']) / Global.OPEN_PRICE - 0.001
            Global.TOTAL *= 1 + diff
            print('%s SHORT: %.1f - %.2f = %.2f%%, value: %.2f' % (t_to_str(Global.OPEN_MIN * 60), Global.OPEN_PRICE, k['high'], diff * 100, Global.TOTAL))
            self.status = Global.NON
            Global.OPEN_PRICE = 0
            Global.OPEN_MIN = 0
            return

        sumvol = sum([x['vol'] for x in self.k[-10:-1]])
        if sumvol == 0:
            return

        vol_impact = (k['buy_vol'] - k['sell_vol']) / sumvol
        if vol_impact > 0.3:
            self.status = Global.LONG
            return
        if vol_impact < -0.3:
            self.status = Global.SHORT

if __name__ == '__main__':
    app = Backtest('dataset.csv')
    app.run()
