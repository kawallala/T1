import sys


M = 5 * 10**6
B = 550

sizeP = 10**4
sizeT = 10**6


def linearSearch(p, T):
    for i in T:
        if p == i:
            return True
        else:
            return False


if __name__ == "__main__":
    Pf = open(sys.argv[1])
    Tf = open(sys.argv[2])

    output = []

    #Pf = open("P.txt", 'r')
    # Tf = open("T.txt", 'r') ?

    P_array = [None for i in range(sizeP)]
    index_P_array = 0
    while True:
        read_chunk = Pf.read(B)
        if not read_chunk:  # se acabó el archivo
            break
        str_numbers = read_chunk.split('\n')
        for str_number in str_numbers:
            # si es que haces conversión a enteros
            P_array[index_P_array] = int(str_number)
            index_P_array += 1

    Pf.close()

    for i in P_array:
        while True:
            read_chunk = Tf.read(B)
            if not read_chunk:   # se acabó el archivo
                break
            str_numbers = read_chunk.split('\n')
            str_numbers = map(int, str_numbers)

            if linearSearch(i, str_numbers):
                output.append(i)
            else:
                break

    Tf.close()

    Of = open("Output.txt", "w")
    for o in output:
        Of.write(o)
    Of.close()
