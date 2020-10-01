import sys

M = 5 * 10**6
B = 550


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

    P_array = []

    while True:
        read_chunk = Pf.read(B)
        if not read_chunk:  # se acabó el archivo
            break
        str_numbers = read_chunk.split('\n')
        # Quitamos elemento final del split TODO refactor
        str_numbers.remove("")
        P_array.extend(list(map(int, str_numbers)))

    Pf.close()

    for i in P_array:
        while True:
            read_chunk = Tf.read(B)
            if not read_chunk:   # se acabó el archivo
                break
            str_numbers = read_chunk.split('\n')
            str_numbers.remove("")
            str_numbers = list(map(int, str_numbers))

            if linearSearch(i, str_numbers):
                output.append(i)

    Tf.close()

    output = list(map(str, output))

    Of = open("Output.txt", "w")
    for o in output:
        Of.write(o)
    Of.close()
