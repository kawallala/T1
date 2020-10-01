import time
import os
import sys

if __name__ == "__main__":
    P = sys.argv[1]
    T = sys.argv[2]
    k_i = int(sys.argv[3])
    k_f = int(sys.argv[4])
    k_step = int(sys.argv[5])
    for k in range(k_i,k_f+k_step,k_step):
        for k2 in range(k):
            # Times.write(str(k)+"\n")
            os.system('python generator.py '+P+' '+T)
            os.system('python binarySearch.py P.txt T.txt ' + str(k))