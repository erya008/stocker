import logging
from time import sleep
import os
import json
import requests 
from dateutil import parser
import datetime
from datetime import tzinfo
from dateutil.tz import tzutc

def dataToFile():
    pass

def schedRun():
    pass

def washData():
    pass


def setupLogger():
    logger = logging.getLogger()
    logger.setLevel('INFO')
    cHandle = logging.StreamHandler()
    cHandle.setFormatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
    logger.addHandler(cHandle)
    return logger

def getTrade():
    #os.environ['http_proxy']='http://127.0.0.1:8899'
    #os.environ['https_proxy']='https://127.0.0.1:8899'
    logger = setupLogger()
    
    header = {
        'content-encoding': 'gzip',
        'content-type': 'application/json; charset=utf-8',
        'status': '200',
        'strict-transport-security': 'max-age=31536000; includeSubDomains',
        'x-powered-by': 'Profit',
        'x-ratelimit-limit': '150',
        'x-ratelimit-remaining': '149',
        'x-ratelimit-reset': '1523885743',
    }
    initstarttime=datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.000Z')# '2018-04-17T01:46:08.487Z'
    l = []
    while(True):
        sleep(1)

        #print("%s\n"%initstarttime)
        try:
            url = requests.get('https://www.bitmex.com/api/v1/trade?count=500&reverse=false&symbol=XBTUSD&startTime=%s' % initstarttime, headers=header) 
        except requests.RequestException as e:
            print(e)
            continue
        else:
            tickers = json.loads(url.text)

        if len(tickers) > 0:
            initstarttime = tickers[-1]['timestamp']

            for ticker in tickers:
                t = ticker['timestamp'][:-5]
                print(l)
                if not l or t != l[-1]['t']:
                    if l:
                        pass#print(l[-1:])
                    a = {'l': 1, 't': t, 'O_price': ticker['price'], 'c_price': ticker['price']}
                    l.append(a)
                else:
                    l[-1]['l'] += 1
                    l[-1]['c_price'] = ticker['price']

        '''
        #while i<len(ticker):
        #print(timestamp)
        #utc2LocalTime = datetime.datetime(2018, 4, 16, 14, 19, 10, 706000, tzinfo=tzutc())
        #print(timestamp)
        print("%s-%s:%s:%s"%(ticker[i]['timestamp'],ticker[i]['side'],ticker[i]['size'],ticker[i]['price'])) 
        i = i+1
        initstarttime = ticker[0]['timestamp']
        '''



if __name__ == "__main__":

    getTrade()