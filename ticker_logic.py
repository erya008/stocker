flagFortickerDensity = 0
flagForVol=0
flagForprice=0


counterForLongperiod = 60*3 //�ж�����
counterForShortperiod = 60*15 //�ж�����

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
 ticker = read(ticker) //�������
 tickerDensity = len(ticker) //��һ���ticker�ܶ�
 Vol=ticker['size']  //��һ��ĳɽ���
 netVol=ticker['Buy']['size']-ticker['sell']['size'] //��һ��ľ��ɽ���
 
 if counterlong<counterForLongperiod :   //�ۼƳ������µ� �ܶ�,������,��������,���۸�(��С�۸�)
  tickerDensityForlongperiod + = tickerDensity
  VolForlongperiod + = vol
  netVolForlongperiod + = netVol
  priceForLongperiod = max(ticker['price'],price)
  
  
 if counterShort<counterForShortperiod:  //�ۼƶ������µ� �ܶ�,������,��������,���۸�(��С�۸�)
  tickerDensityForshortperiod + = tickerDensity
  VolForshortperiod + = vol
  netVolForshortperiod + = netVol
  priceForshortperiod = max(ticker['price'],price)
  
  if tickerDensity > tickerDensityForlongperiod/counterlong and tickerDensity>tickerDensityForshortperiod/counterShort and tickerDensityForshortperiod/counterShort  > tickerDensityForlongperiod/counterlong:
   '''
   ��ǰ���ܶȴ��ڳ����ڵ�ƽ���ܶȺͶ����ڵ�ƽ���ܶ�,�Ҷ����ڵ�ƽ���ܶȴ��ڳ����ڵ�ƽ���ܶ�
   ��ʾ�����ȶ�����
   
   '''
   flagFortickerDensity =1   
  if ticker['price']>priceForLongperiod and ticker['price']>priceForshortperiod and priceForLongperiod>priceForshortperiod:
   '''
   ��ǰ�ļ۸��ڳ����ڵĺͶ����ڵ���߼�,�Ҷ����ڵ���߼۸���ڳ����ڵ���߼۸�
   ��ʾ����ͻ��
   
   ���շ����߼�
  
   '''   
   flagForprice +=1
  
   counterShort +=1
   counterlong +=1  
 
 else: 
  counterShort=0
  counterlong =0 
  return flagFortickerDensity,priceForshortperiod
     