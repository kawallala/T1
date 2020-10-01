import sys
import time

M = 5 * 10**6
B = 550
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

    for i in P_array:
        while True:
            read_chunk = Tf.read(B)
            if not read_chunk:   # se acabó el archivo
                break
            str_numbers = read_chunk.split('\n')
            str_numbers.remove("")
            IO_count += 1

            if linearSearch(i, str_numbers):
                output.append(i+"\n")

    Tf.close()

    Of = open("Results/Output.txt", "w")
    for o in output:
        Of.write(o)
        IO_count += 1
    Of.close()

    end_time = time.time()
    print(end_time-start_time)
    Times = open("Results/TimesLinear.txt", "w")
    Times.write(str(end_time-start_time) + "\n")
    Times.close

    IO = open("Results/IOLinear.txt", "w")
    IO.write(str(IO_count) + "\n")
    IO.close
