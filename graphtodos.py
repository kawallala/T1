from matplotlib import pyplot as plt
import numpy as np
import sys

if __name__ == "__main__":
    Times_all = [[None for i in range(3)] for i in range(4)]
    IOs_all = [[None for i in range(3)] for i in range(4)]
    Times_all_std = [[None for i in range(3)] for i in range(4)]
    IOs_all_std = [[None for i in range(3)] for i in range(4)]
    names = ['Binary', 'Index', 'LinearBinary', 'LinearMerge']
    for i in range(3):
        for j in range(4):
            Tf = open("Results_Experimento/TimesAndCount" + names[j] + str(i) + ".txt", newline='\n')
            results = Tf.readlines()
            Times = []
            IOs = []
            for result in results:
                result = result.split(' ')
                Times.append(float(result[0]))
                IOs.append(int(result[1]))
            Times_all[j][i] = np.mean(np.array(Times))
            IOs_all[j][i] = np.mean(np.array(IOs))
            Times_all_std[j][i] = np.std(np.array(Times))
            IOs_all_std[j][i] = np.std(np.array(IOs))
    
    names = ['|T|/2','|T|/4', '|T|/6']
    plt.title('Búsqueda Lineal + Merge se ejecuta en el menor tiempo')
    plt.plot(names, Times_all[:][2], label='Lineal + Binaria', marker='o' )
    plt.plot(names, Times_all[:][0], label= 'Binaria', marker = 'o')
    plt.plot(names, Times_all[:][1], label = 'Indexada', marker = 'o') 
    plt.plot(names, Times_all[:][3], label='Lineal + Merge', marker='o' )
    plt.xlabel("Valor de |P|")
    plt.ylabel("Tiempo de ejecución [s]")
    plt.legend()
    # plt.yscale('log')
    plt.savefig("Tiempo_ejecucion")


    # plt.title('Búsqueda lineal realiza el menor número de operaciones IO')
    # plt.plot(names, IOs_all[:][0], label= 'Binaria', marker = 'o')
    # plt.plot(names, IOs_all[:][1],  label = 'Indexada', marker = 'o')
    # plt.plot(names, IOs_all[:][2],  label='Lineal', marker = 'o')
    # plt.xlabel("Valor de |P|")
    # plt.ylabel("Operaciones IO")
    # plt.yscale('log')
    # plt.legend()
    # plt.savefig("Operaciones_IO")

