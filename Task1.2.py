#import math for using sqrt
from math import sqrt

def Loops():
    #set four loops, the first and second represent the first point,
    #the rest loops represent the target point
    for i in range(8):
        for z in range(8): 
            for m in range(8):
                for n in range(8):
                    d=sqrt((n-z)**2+(m-i)**2)
                    #when distance is eauql to 0, it jump out of upper
                    #loop
                    if(d==0):
                        break
                    print((z+1,i+1),"to",(n+1,m+1),"distance",d)
        
Loops()