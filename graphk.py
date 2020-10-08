from matplotlib import pyplot as plt
import numpy as np
import sys

if __name__ == "__main__":
    k_i = int(sys.argv[1])
    k_f = int(sys.argv[2])
    k_step = int(sys.argv[3])
    T_all = []
    for k in range(k_i,k_f+k_step,k_step):
        T_temp = []
        for i in range(10):
            Tf = open("Results/Times" + str(k) + "_"+ str(i) + ".txt")
            T = [float(t) for t in Tf.readlines()]
            T_np = np.array(T)
            T_temp.append(np.mean(T_np))
        T_all.append(T_temp)
    T_all_np = [np.array(t) for t in T_all]
    T_all_mean = [np.mean(t) for t in T_all_np]
    T_all_std = [np.std(t) for t in T_all_np]
    ks = np.linspace(k_i,k_f,k_step)
    plt.errorbar(ks, T_all_mean, T_all_std, ls = '')
    plt.show()
