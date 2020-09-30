import time
import os
import sys

if __name__ == "__main__":
    P = sys.argv[1]
    T = sys.argv[2]
    k = sys.argv[3]
    # times = []
    for _ in range(int(k)):
        os.system('python generator.py '+P+' '+T)
        # start_time = time.time()
        os.system('python binarySearch.py P.txt T.txt')
        # end_time = time.time()
        # times.append(end_time-start_time)
    # print(times)