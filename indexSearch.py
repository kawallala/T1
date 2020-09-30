import sys


M = 5 * 10**6
B = 550

def Bin(i, arr, index):
    if len(arr) != 0:
        temp = arr[len(arr)//2]
        if i > temp:
            Bin(i, arr[len(arr)//2:len(arr)], index + index//2)
        else:
            if i < temp:
                Bin(i, arr[0:len(arr)//2 -1], index - index//2)
            else:
                return index
    else:
        return index
        
if __name__ == "__main__":
    S = []
    output = []
    Pf = open(sys.argv[1])
    Tf = open(sys.argv[2])
    T = Tf.readlines()
    for i in range(0, len(T) - B, B):
        S.append(T[i])
    P = Pf.readlines()
    for j in range(0, len(P)):
        print(Bin(P[j], S, len(S)//2))
        index = Bin(P[j], S, len(S)//2) * B
        for i in range(index, index+B):
            if T[index] == P[j]:
                output.append(P[j])
    Pf.close()
    Of = open("Output.txt","w")
    for o in output:
        Of.write(o)
    Of.close()