import sys
import time

M = 5 * 10**6
B = 500
IO_count = 0
Comp = 0


def binarySearch(p, str_numbers):
    global Comp
    l = 0
    r = len(str_numbers) - 1
    while l<r:
        m = (l+r)//2 + 1
        c = str_numbers[m]
        Comp +=1
        if p < c:
            r = m - 1
        elif p > c:
            l = m
        else:
            return True
    return False


if __name__ == "__main__":
    start_time = time.time()
    Pf = open(sys.argv[1])
    Tf = open(sys.argv[2])

    output = []

    P_array = []

    while True:
        read_chunk = Pf.read(B)
        if not read_chunk:  # se acabó el archivo
            break
        str_numbers = read_chunk.split('\n')
        # Quitamos elemento final del split TODO refactor
        str_numbers.pop()
        P_array.extend(str_numbers)
        IO_count += 1

    Pf.close()

    while True:
        read_chunk = Tf.read(B)
        if not read_chunk:   # se acabó el archivo
            break
        str_numbers = read_chunk.split('\n')
        str_numbers.pop()
        IO_count += 1
        for p in P_array:
            if binarySearch(p, str_numbers):
                output.append(''.join([p, '\n']))

    Tf.close()

    output = "".join(output)
    Of = open("Results/Output.txt", "a")
    number_blocks = max(len(output) // B,1)
    for i in range(number_blocks):
        Of.write(output[i*B:(i+1)*B])
        IO_count += 1
    Of.close()

    end_time = time.time()

    if len(sys.argv) == 4:
        Times = open("Results/TimesAndCountLinearBinary" + sys.argv[3] + ".txt", 'a')
        Times.write(str(end_time-start_time) + ' ' + str(IO_count) + "\n")
    else:
        Times = open("Results/TimeAndCountLinearBinary.txt", 'w')
        Times.write(str(end_time-start_time) + ' ' + str(IO_count))
    Times.close()
