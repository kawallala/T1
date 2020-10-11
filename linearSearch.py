import sys
import time

M = 5 * 10**6
B = 500
IO_count = 0
Comp = 0

def linearSearch(p, T):
    global Comp
    for i in T:
        Comp += 1
        if p == i:
            return True


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

        for i in str_numbers:
            if linearSearch(i, P_array):
                output.append(i+"\n")

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
        Times = open("Results/TimesAndCountLinear" + sys.argv[3] + ".txt", 'a')
        Times.write(str(end_time-start_time) + ' ' + str(IO_count) + "\n")
    else:
        Times = open("Results/TimeAndCountLinear.txt", 'a')
        Times.write(str(end_time-start_time) + ' ' + str(IO_count))
    Times.close()
