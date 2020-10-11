import time
import os
import sys
import generator
import binarySearch
import linearSearch
import indexSearch

if __name__ == "__main__":
    sizeT = int(sys.argv[1])
    sizeP = [sizeT//2, sizeT//4, sizeT//6]
    #  |P| < |T|/3     |P| > |T|/3     |P| > |T|/7
    k = 15
    for i in range(3):
        for j in range(k):
            print("generando")
            os.system("python generator.py " + str(sizeP[i]) + ' ' + str(sizeT)) 
            print("buscando LinearBinary")
            os.system("python linearBinarySearch.py P.txt T.txt " + str(i))
            print("Buscando LinearMerge")
            os.system("python linearMergeSearch.py P.txt T.txt " + str(i))
            print("Buscando Linear")
            os.system("python linearSearch.py P.txt T.txt " + str(i))
            print("terminado ciclo")