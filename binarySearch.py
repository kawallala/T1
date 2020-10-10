import sys
import os
import linecache
import time
M = 5 * 10**6
B = 500
C = 0

def read_block(file, position = None):
    global C
    file.seek(0)
    if position:
        file.seek(position)
    block = file.read(B)
    C += 1
    return block


def binarySearch(file, filename, size_file, str_element):
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
    T_name = sys.argv[2]
    file = open(T_name)
    size_file = os.path.getsize(T_name)
    output = []
    current_block = 0
    while(True):
        blockP = read_block(Pf,current_block)
        if not blockP:
            break
        current_block += B + B//10
        str_numbers = blockP.split('\n')
        str_numbers.pop()
        for p in str_numbers: 
            if binarySearch(file, T_name, size_file, p):
                output.append(''.join([p,'\n']))
    Pf.close()

    output = "".join(output)
    Of = open("Results/Output.txt", "a")
    number_blocks = max(len(output) // B,1)
    for i in range(number_blocks):
        Of.write(output[i*B:(i+1)*B])
        C += 1
    Of.close()

    end_time = time.time()
    if len(sys.argv) == 4:
        r = sys.argv[3]
        Times = open("Results/TimesAndCountBinary" + r + ".txt", 'a')
        Times.write(str(end_time-start_time) + ' ' + str(C) + "\n")
    else:
        Times = open("Results/TimeAndCountBinary" + sys.argv[3] + ".txt", 'a')
        Times.write(str(end_time-start_time) + ' ' + str(C))
    Times.close()