import sys
import time

M = 5 * 10**6
B = 500
IO_count = 0


def merge(str_numbers, P_array):
    i = 0
    j = 0
    merged_list = []
    while i<len(str_numbers) and j< len(P_array):
        if str_numbers[i]<P_array[j]:
            i += 1
        elif str_numbers[i]>P_array[j]:
            j += 1
        else:
            merged_list.append(''.join([str_numbers[i], '\n']))
            i+=1
            j+=1
    return merged_list

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
    P_array.sort()
    while True:
        read_chunk = Tf.read(B)
        if not read_chunk:   # se acabó el archivo
            break
        str_numbers = read_chunk.split('\n')
        str_numbers.pop()
        IO_count += 1
        output.extend(merge(str_numbers,P_array))

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
        Times = open("Results/TimesAndCountLinearMerge" + sys.argv[3] + ".txt", 'a')
        Times.write(str(end_time-start_time) + ' ' + str(IO_count) + "\n")
    else:
        Times = open("Results/TimeAndCountLinearMerge.txt", 'w')
        Times.write(str(end_time-start_time) + ' ' + str(IO_count))
    Times.close()
