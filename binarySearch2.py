import os
import time
import sys
B = 550
FILENAME = "T.txt"
IO_COUNT = 0

def read_block(filename, position = None):
        global IO_COUNT
        with open(filename, 'r') as f:
            if position:
                f.seek(position)
            block = f.read(B)
        IO_COUNT += 1
        return block

def read_file(filename):
    global IO_COUNT
    file_content_array = []
    with open(filename, 'r') as f:
        while True:
            block = f.read(B)
            if not block:
                break
            IO_COUNT += 1
            file_content_array.append(block)
    return ''.join(file_content_array)

def binary_search(str_element):
    size_file = os.path.getsize(FILENAME)
    number_blocks = size_file // B
    l = 0
    r = number_blocks -1
    while l != r:
        m = (l+r) // 2
        position_to_read = m*B
        block = read_block(FILENAME, position_to_read)
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
            l = m + 1
    position_to_read = l*B
    block = read_block(FILENAME, position_to_read)
    return str_element in block.split('\n')

if __name__ == "__main__":
    start_time = time.time()
    Pf = open(sys.argv[1])
    output = []
    while(True):
        p = Pf.readline()
        IO_COUNT += 1
        if p =="":
            break
        if binary_search(p):
            output.append(p)
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
        Times.write(str(end_time-start_time) + ' ' + str(IO_COUNT))
    Times.close()