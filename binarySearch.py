import sys
import os
import linecache
import time
M = 5 * 10**6
B = 550

def binarySearch(p, Ti, Tf, Ts):
    temp_i = (Tf+Ti)//2
    if Tf>Ti:
        temp = linecache.getline(Ts, temp_i + 1)
        if p> temp:
            return binarySearch(p, temp_i+1, Tf, Ts)
        else:
            if p<temp:
                return binarySearch(p, Ti, temp_i - 1, Ts)
            else:
                return True
    else:
        return False



if __name__ == "__main__":
    start_time = time.time()
    Pf = open(sys.argv[1])
    Tf = os.stat(sys.argv[2]).st_size//11
    output = []
    while(True):
        p = Pf.readline()
        if p =="":
            break
        if binarySearch(p, 0, Tf, sys.argv[2]):
            output.append(p)
    Pf.close()
    Of = open("Output.txt","w")
    for o in output:
        Of.write(o)
    Of.close()
    end_time = time.time()
    if len(sys.argv) == 4:
        r = sys.argv[3]
        Times = open("Results/Times"+r+".txt", 'a')
        Times.write(str(end_time-start_time) + "\n")
    else:
        print(end_time-start_time)