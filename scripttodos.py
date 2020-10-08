import time
import os
import sys
import generator
import binarySearch
import linearSearch
import indexSearch
if __name__ == "__main__":
    sizeT = sys.argv[1]
    sizeP = [sizeT//4, sizeT//2, sizeT//6]
    #  |P| < |T|/3     |P| > |T|/3     |P| > |T|/7
    k = 15
    for i in range(3):
        for j in range(k):
            print("generando")
            os.system("python generator.py " + str(sizeP[i]) + ' ' + str(sizeT)) 
            print("buscando")
            os.system("python binarySearch.py P.txt T.txt " + str(i))
            os.system("python indexSearch.py P.txt T.txt " + str(i))
            os.system("python linearSearch.py P.txt T.txt " + str(i))
            print("terminado ciclo")