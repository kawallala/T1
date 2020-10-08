import sys
import os
import linecache
import time
M = 5 * 10**6
B = 10
C = 0

def read_block(file, position = None):
    global C
    file.seek(0)
    if position:
        file.seek(position)
    block = file.read(B)
    C += 1
    return block


def binarySearch(filename, str_element):
    size_file = os.path.getsize(filename)
    file = open(filename)
    number_blocks = max(size_file // (B+ B//10), 1)
    l = 0
    r = number_blocks -1
    while l < r:
        m = (l+r) // 2 + 1
        position_to_read = m*(B+B//10)
        block = read_block(file, position_to_read)
        str_numbers = block.split('\n')
        str_numbers.pop()
        if str_element in str_numbers:
            return True
        first_block = str_numbers[0]
        last_block = str_numbers[-1]
        if last_block >= str_element >= first_block :
            return False
        if str_element < first_block:
            r = m - 1
        else:
            l = m
    position_to_read = l*(B+B//10)
    block = read_block(file, position_to_read)
    return str_element in block.split('\n')


if __name__ == "__main__":
    start_time = time.time()
    Pf = open(sys.argv[1])
    Tf = os.stat(sys.argv[2]).st_size//11
    output = []
    current_block = 0
    while(True):
        blockP = read_block(Pf,current_block)
        C += 1
        if not blockP:
            break
        current_block += B + B//10
        str_numbers = blockP.split('\n')
        str_numbers.pop()
        for p in str_numbers: 
            if binarySearch(sys.argv[2], p):
                output.append(p)
                output.append('\n')
    Pf.close()
    Of = open("Output.txt","w")
    for o in output:
        Of.write(o)
    Of.close()
    end_time = time.time()
    if len(sys.argv) == 5:
        r = sys.argv[3]
        i = sys.argv[4]
        Times = open("Results/Times"+r+"_"+i+".txt", 'a')
        Times.write(str(end_time-start_time) + "\n")
    else:
        Times = open("Results/TimeAndCountBinary.txt", 'w')
        Times.write(str(end_time-start_time) + ' ' + str(C))
    Times.close()