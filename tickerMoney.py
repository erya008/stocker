import csv

def initVar():
    var={}
    var['flagFortickerDensity'] = 0
    var['flagForVol']=0
    var['flagForprice']=0
    
    
    var['counterForLongperiod'] = 60*15
    var['counterForShortperiod'] = 60*3
    
    var['counterLong'] = 0 
    var['counterShort'] = 0 
    
    var['tickerDensity'] = 0
    var['tickerDensityForlongperiod']=0
    var['tickerDensityForshortperiod']=0
    
    var['Vol'] =0
    var['VolForlongperiod'] =0
    var['VolForshortperiod']=0
    
    var['netVol'] =0
    var['netVolForlongperiod']=0
    var['netVolForshortperiod']=0
    
    
    var['price']=0
    var['priceForLongperiod'] =0
    var['priceForshortperiod'] =0   

    return var

def getTrade():
    
    import csv
    var = initVar()
    pretimestamp='2017-01-01T00:00:36'
    
    
    with open('dataframe.csv',encoding='utf-8') as csvfile:
        reader=csv.reader(csvfile)
        
        for i,rows in enumerate(reader):
            '''
            read one line from csv and call func to handle
            '''

            
            if (var['tickerDensity']>var['tickerDensityForlongperiod']/var['counterForLongperiod']      and 
                var['tickerDensity']>var['tickerDensityForshortperiod']/var['counterForShortperiod']  and  
                var['tickerDensityForshortperiod']/var['counterForShortperiod']>var['tickerDensityForlongperiod']/var['counterForLongperiod'] and 
                float(rows[3]) >var['priceForLongperiod']  and
               float(rows[3]) >var['priceForshortperiod'] and
                var['priceForshortperiod']>var['priceForLongperiod']                
                ):
                print (float(rows[3]) ,var['priceForLongperiod'] , var['priceForshortperiod'] ,var['priceForshortperiod'],var['priceForLongperiod']  ,var['tickerDensity'],var['tickerDensityForlongperiod']/var['counterForLongperiod'] ,var['tickerDensityForshortperiod']/var['counterForShortperiod'],
                       var['tickerDensityForshortperiod']/var['counterForShortperiod'],var['tickerDensityForlongperiod']/var['counterForLongperiod'] ,rows[-2])
               
            
         
            
                
               
            
            if i==0:
                pass
            else:
                #print(rows)
                if pretimestamp== rows[-2][:-5] :
                    if var['price']<float(rows[3]) :
                        var['price'] = float(rows[3]) 
                    var['tickerDensity'] +=float(rows[5])
                    if var['counterLong']<var['counterForLongperiod']:
                        var['tickerDensityForlongperiod']+=float(rows[5])
                        
                        if var['priceForLongperiod']< float(rows[3]):
                            var['priceForLongperiod'] = float(rows[3]) 
                    else:
                        var['counterLong']=0
                        var['tickerDensityForlongperiod']=0
                        var['priceForLongperiod'] = float(rows[3])   
                        
                        
                        
                        
                    if var['counterShort']<var['counterForShortperiod']:
                        var['tickerDensityForshortperiod']+=float(rows[5])
                        
                        if var['priceForshortperiod']< float(rows[3]):
                            var['priceForshortperiod']=float(rows[3])
                    else:
                        var['counterShort'] =0
                        var['tickerDensityForshortperiod']=0
                        var['priceForshortperiod']=float(rows[3]) 
                     
                    
                        
                else:
                    pretimestamp = rows[-2][:-5]
                    var['tickerDensity']=float(rows[5])
                    var['counterLong']+=1
                    var['counterShort']+=1

                    #if(rows[-2][:-5])
                #print(var)

    ''' 

#csv_reader=csv.reader(open('dataframe.csv',encoding='utf-8'))
#for row in csv_reader:
#    print(row)
'''   
if __name__ == "__main__":

    getTrade()