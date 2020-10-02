import sys
import os
import linecache


M = 5 * 10**6
B = 550


def Bin(i, arr, index, indexf):
    if (indexf-index) > 0:
        temp_i = (indexf+index)//2 + 1
        temp = arr[temp_i]
        if i > temp:
            return Bin(i, arr, temp_i, indexf) #No va temp_i + 1 porque temp_i sigue siendo un candidato
        else:
            if i < temp:
                return Bin(i, arr, index, temp_i - 1) #Si va el -1 pq temp_i ya no es candidato
            else:
                return temp_i
    else:
        return index
        
if __name__ == "__main__":
    S = []
    output = []
    Pf = open(sys.argv[1])
    Tf = os.stat(sys.argv[2]).st_size//11  #tamaño del T
    for i in range(0, Tf, B//11):
        temp = linecache.getline(sys.argv[2], i + 1) # +1 porque parte en 1
        S.append(temp)

    while(True):
        p = Pf.readline()
        if p =="":
            break
        index = Bin(p, S, 0, len(S)-1) #ayuda pq temp_i es none
        for i in range(index*B//11, (index+1)*B//11):
            if linecache.getline(sys.argv[2], i + 1) == p:
                output.append(p)
    Pf.close()

    Of = open("Output.txt","w")
    for o in output:
        Of.write(o)
    Of.close()