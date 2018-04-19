import csv
import time
import datetime
import string
'''

class TickerBase(object):
    def __init__(self):
        pass
    
    def returnTick(*kw):
        return kw

        

class Ticker(TickerBase):

    def __init__(self):
        pass
    
'''
def onticker():
    with open('l:\\dataset.csv',encoding='utf-8') as csvfile:
        reader=csv.reader(csvfile)
        counter =0
        sumvol =[]
        openBPrice=0
        openSPrice=0
        profit=0
        netvolpluase=0.0
        x,x1,x2=(0,0,0)
        for i,rows in enumerate(reader):
            if i==0:
                pass
            else:
               
                if(counter<10):
                    counter+=1
                    sumvol.append(float(rows[15]))
                else:
                    del sumvol[0]
                    sumvol.append(float(rows[15]))
                    #print(sumvol)
                if(i>10):
                    
                    if sum(sumvol)==0 :
                        pass
                    else:
                        netvolpluase = (float(rows[5]))/sum(sumvol)        
                        if netvolpluase>0.3 and i-x1>3:
                            #print(rows)
                            openBPrice=float(rows[0])
                            x1 =i
                        elif netvolpluase<-0.3 and i-x2>3:
                            #print(rows)
                            openSPrice=float(rows[0])
                            x2=i
               
               
                if(i-x1==2 and openBPrice>0): #duixiang lirun
                    profit+= float(rows[0])-openBPrice
                    x1=0
                if(i-x2==2 and openSPrice>0):
                    profit+= openSPrice -float(rows[0])
                    x2=0
        
                
        
        
            print(profit)
            
if __name__ == "__main__":

    onticker()