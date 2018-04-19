flagFortickerDensity = 0
flagForVol=0
flagForprice=0


counterForLongperiod = 60*3 //判断周期
counterForShortperiod = 60*15 //判断周期

counterLong = 0 
counterShort = 0 

tickerDensity = 0
tickerDensityForlongperiod =0
tickerDensityForshortperiod=0

Vol =0
VolForlongperiod =0
VolForshortperiod=0

netVol =0
netVolForlongperiod=0
netVolForshortperiod=0


price =0
priceForLongperiod =0
priceForshortperiod =0

netVol=0

while(1):
 ticker = read(ticker) //按秒读入
 tickerDensity = len(ticker) //这一秒的ticker密度
 Vol=ticker['size']  //这一秒的成交量
 netVol=ticker['Buy']['size']-ticker['sell']['size'] //这一秒的净成交量
 
 if counterlong<counterForLongperiod :   //累计长周期下得 密度,交易量,净交易量,最大价格(最小价格)
  tickerDensityForlongperiod + = tickerDensity
  VolForlongperiod + = vol
  netVolForlongperiod + = netVol
  priceForLongperiod = max(ticker['price'],price)
  
  
 if counterShort<counterForShortperiod:  //累计短周期下得 密度,交易量,净交易量,最大价格(最小价格)
  tickerDensityForshortperiod + = tickerDensity
  VolForshortperiod + = vol
  netVolForshortperiod + = netVol
  priceForshortperiod = max(ticker['price'],price)
  
  if tickerDensity > tickerDensityForlongperiod/counterlong and tickerDensity>tickerDensityForshortperiod/counterShort and tickerDensityForshortperiod/counterShort  > tickerDensityForlongperiod/counterlong:
   '''
   当前的密度大于长周期的平均密度和短周期的平均密度,且短周期的平均密度大于长周期的平均密度
   显示行情热度升温
   
   '''
   flagFortickerDensity =1   
  if ticker['price']>priceForLongperiod and ticker['price']>priceForshortperiod and priceForLongperiod>priceForshortperiod:
   '''
   当前的价格于长周期的和短周期的最高价,且短周期的最高价格大于长周期的最高价格
   显示行情突破
   
   做空反向逻辑
  
   '''   
   flagForprice +=1
  
   counterShort +=1
   counterlong +=1  
 
 else: 
  counterShort=0
  counterlong =0 
  return flagFortickerDensity,priceForshortperiod
     