import sys
import time

M = 5 * 10**6
B = 500
IO_count = 0


def linearSearch(p, T):
    for i in T:
        if p == i:
            return True
        else:
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
        str_numbers.remove("")
        P_array.extend(str_numbers)
        IO_count += 1

    Pf.close()

    while True:
        read_chunk = Tf.read(B)
        if not read_chunk:   # se acabó el archivo
            break
        str_numbers = read_chunk.split('\n')
        str_numbers.remove("")
        IO_count += 1

        for i in str_numbers:
            if linearSearch(i, P_array):
                output.append(i+"\n")

    Tf.close()

    Of = open("Results/Output.txt", "a")
    for o in output:
        Of.write(o)
        IO_count += 1
    Of.close()

    end_time = time.time()

    if len(sys.argv) == 4:
        Times = open("Results/TimesAndCountLinear" + sys.argv[3] + ".txt", 'a')
        Times.write(str(end_time-start_time) + ' ' + str(IO_count) + "\n")
    else:
        Times = open("Results/TimeAndCountLinear.txt", 'w')
        Times.write(str(end_time-start_time) + ' ' + str(IO_count))
    Times.close()
