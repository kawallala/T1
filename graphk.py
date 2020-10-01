import matplotlib
import numpy as np
import sys

if __name__ == "__main__":
    k_i = int(sys.argv[1])
    k_f = int(sys.argv[2])
    k_step = int(sys.argv[3])
    for k in range(k_i,k_f+k_step,k_step):
        Tf