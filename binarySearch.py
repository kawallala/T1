import sys
import os
import linecache
M = 5 * 10**6
B = 500

def binarySearch(p, Ti, Tf, Ts):
    temp_i = (Tf-Ti)//2
    if temp_i >= 0:
        temp = linecache.getline(Ts, temp_i + 1)
        if p> temp:
            return binarySearch(p, temp_i + 1, Tf, Ts)
        else:
            if p<temp:
                return binarySearch(p, Ti, temp_i - 1, Ts)
            else:
                return True
    return False



if __name__ == "__main__":
    Pf = open(sys.argv[1])
    Tf = os.stat(sys.argv[2]).st_size//11 - 1
    output = []
    while(True):
        p = Pf.readline()
        if p =="":
            break
        if binarySearch(p, 1, Tf, sys.argv[2]):
            output.append(p)
    Pf.close()
    Of = open("Output.txt","w")
    for o in output:
        Of.write(o)
    Of.close()
