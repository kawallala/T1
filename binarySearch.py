import sys


M = 5 * 10**6
B = 500

def binarySearch(p, T):
    if len(T)!= 0:
        temp = T[len(T)//2]
        if p> temp:
            return binarySearch(p, T[len(T)//2+1:])
        else:
            if p<temp:
                return binarySearch(p, T[:len(T)//2])
            else:
                return True
    else:
        return False



if __name__ == "__main__":
    Pf = open(sys.argv[1])
    Tf = open(sys.argv[2])
    T = Tf.readlines()
    Tf.close()
    output = []
    while(True):
        p = Pf.readline()
        if p =="":
            break
        if binarySearch(p,T):
            output.append(p)
    Pf.close()
    Of = open("Output.txt","w")
    for o in output:
        Of.write(o)
    Of.close()
