import sys
import os
import linecache
import time


M = 5 * 10**6
B = 20
C = 0   #El contador de IOs

def read_block(file, position = None):
    global C
    file.seek(0)
    if position:
        file.seek(position)
    block = file.read(B)
    C += 1
    return block

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
    start_time = time.time()
    S = []
    output = []
    Pf = open(sys.argv[1])
    Tf = open(sys.argv[2])
    size_file = os.path.getsize(sys.argv[2])
    number_blocks = max(size_file // (B+B//10), 1)
    for i in range(number_blocks):
        block = read_block(Tf, i*(B+B//10))
        S.append(block.split('\n')[0])

    P_array = []
    current_block = 0
    while(True):
        blockP = read_block(Pf, current_block)
        current_block += B+(B//10)
        if not blockP: # se acabó el archivo
            break
        str_numbers = blockP.split('\n')
        str_numbers.pop()
        P_array.extend(str_numbers)
   
    Pf.close()

    for p in P_array:
            index = Bin(p, S, 0, len(S)-1)
            blockT = read_block(Tf,index*(B+B//10)) 
            if p in blockT.split('\n'):
                output.append(p)
                output.append('\n')

    Of = open("Output.txt","w")
    for o in output:
        Of.write(o)
    Of.close()

    end_time = time.time()
    print(end_time-start_time)
    Times = open("Results/TimesIndex.txt", "w")
    Times.write(str(end_time-start_time) + "\n")
    Times.close

    IO = open("Results/IOIndex.txt", "w")
    IO.write(str(C) + "\n")
    IO.close