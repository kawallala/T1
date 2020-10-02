from matplotlib import pyplot as plt
import numpy as np
import sys

if __name__ == "__main__":
    k_i = int(sys.argv[1])
    k_f = int(sys.argv[2])
    k_step = int(sys.argv[3])
    T_all = []
    for k in range(k_i,k_f+k_step,k_step):
        Tf = open("Results/Times" + str(k) + ".txt")
        T = [float(t) for t in Tf.readlines()]
        T_all.append(T)
    T_all_np = [np.array(t) for t in T_all]
    T_all_var = [np.var(t) for t in T_all_np]
    ks = np.linspace(k_i,k_f,k_step)
    t = []
    plt.bar(ks, T_all_var)
    plt.show()
