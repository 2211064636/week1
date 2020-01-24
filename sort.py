#creat a list of random number
import random
import numpy as ny
def random_integers(extent,number):
    x=random.sample(range(extent),number)   
    return x

#save these number into a list
K=[]
K=random_integers(100,30)
print(K)

#sort a list of integers
def sort():
    L=list()
    for i in range(len(K)):
        m=ny.min(K)
        L.append(m)
        K.remove(m)
    print(L)
sort()   