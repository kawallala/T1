from matplotlib import pyplot as plt
import numpy as np
import sys

if __name__ == "__main__":
    Times_all = [[None for i in range(3)] for i in range(3)]
    IOs_all = [[None for i in range(3)] for i in range(3)]
    Times_all_std = [[None for i in range(3)] for i in range(3)]
    IOs_all_std = [[None for i in range(3)] for i in range(3)]
    names = ['Binary', 'Index', 'Linear']
    for i in range(3):
        for j in range(3):
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
    # plt.title('Variacion tiempo de ejecucion')
    # plt.scatter(names, Times_all[:][0], label= 'Binaria')
    # plt.scatter(names, Times_all[:][1], label = 'Indexada')
    # plt.scatter(names, Times_all[:][2], label='Lineal')
    # plt.xlabel("Valor de |P|")
    # plt.ylabel("Tiempo de ejecución")
    # plt.legend()
    # plt.yscale('log')
    # plt.savefig("Tiempo_ejecucion")


    plt.title('Variacion operaciones IO')
    plt.scatter(names, IOs_all[:][0], label= 'Binaria')
    plt.scatter(names, IOs_all[:][1],  label = 'Indexada')
    plt.scatter(names, IOs_all[:][2],  label='Lineal')
    plt.xlabel("Valor de |P|")
    plt.ylabel("Operaciones IO")
    plt.yscale('log')
    plt.legend()
    plt.savefig("Operaciones_IO")

