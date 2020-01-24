#generate random list
import random

def random_list(points_number=10,x=0.0,y=2.0):
    
    value=[]
    
    for i in range(points_number):      
        value.append(random.uniform(x,y))
    
    return value

print(random_list())

print(random_list(20,10,50))