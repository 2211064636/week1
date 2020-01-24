#use double loop to output every coordinates in the chessboard

#also caculate the whole running time
import time
#start time
t=time.clock()

def Loops():
    for i in range(8):
        for z in range(8):        
            print((z+1,i+1))
        
Loops()
#end time
t=time.clock()-t
print(t)

        
