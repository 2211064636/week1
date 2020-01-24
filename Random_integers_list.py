#generate many random integers 

import random

def random_integers(extent,number):
    x=random.sample(range(extent),number)   
    return x

print(random_integers(100,3))
