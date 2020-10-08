import time
import os
import sys
import generator
import binarySearch
if __name__ == "__main__":
    P = sys.argv[1]
    T = sys.argv[2]
    k_i = int(sys.argv[3])
    k_f = int(sys.argv[4])
    k_step = int(sys.argv[5])
    for k in range(k_i,k_f+k_step,k_step):
        for i in range(10):
            for k2 in range(k):
                print("generando")
                os.system("python generator.py 10000 1000000")
                print("buscando")
                os.system("python binarySearch.py P.txt T.txt " + str(k) + ' ' + str(i))
                print("terminado ciclo")