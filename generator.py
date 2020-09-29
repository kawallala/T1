import sys
import random
def gen_P(size) :
    f = open("P.txt", "w")
    for _ in range(size):
        f.write(str(random.randrange(1,10**9)).zfill(9)+ "\n")
def gen_N(size):
    T = []
    for _ in range(size):
        T.append(random.randrange(1,10**9))
    T.sort()
    f = open("T.txt", "w")
    for t in T:
        f.write(str(t).zfill(9)+"\n")
if __name__ == "__main__":
    P = sys.argv[1]
    T = sys.argv[2]
    gen_P(int(P))
    gen_N(int(T))
    