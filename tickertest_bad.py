import csv
from matplotlib  import pyplot


pt= pyplot.plot()
def onticker():
    volsum=[]
    Bprice,Sprice,profit,i,x1,x2,j,k=(0,0,0,0,0,0,0,0)
    netvolimpact=0.0
    counter=0
    
    
    with open ('dataset.csv',encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for i,rows in enumerate(reader):
            if i==0:
                pass
            else:
                
                if(counter<9):
                    volsum.append(float(rows[15]))
                    counter+=1
                else:
                    del volsum[0]
                    volsum.append(float(rows[15]))
                    netvolimpact = float(rows[5])/(sum(volsum)+1)
                    
                    if netvolimpact>0.5  and i-x1>5 :
                        Bprice=float(rows[0])
                        x1=i     
                        #print(rows)
                        
                    elif netvolimpact<-0.5 and i-x2>5:
                        Bprice=float(rows[0])
                        x2=i 
                                            
                    if i-x1==3 and Bprice>0 and (float(rows[0])-Bprice)/Bprice>0.004:
                        profit += float(rows[0])-Bprice
                        Bprice=0
                        x1=0
                        j+=1
                        #print(rows)
                    if i-x2==3 and Sprice>0 and (Sprice-float(rows[0]))/Sprice>0.004:
                        profit += Sprice-float(rows[0])
                        Sprice=0
                        x2=0
                        k+=1
                        #print(rows)
                   
            print("count buy : %d ,count sell: %d"%(j,k))
    
                        
                        
                    
                    
                    
                    
               
    
        
    
    
    
    
    
                
if  __name__=="__main__":
    onticker()
    