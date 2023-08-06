import numpy as np
import matplotlib.pyplot as plt
import os
import random
if __name__ == "__main__" :
    for l in range(4):
      for i in range(10):
        n = pow(10,l+1)
        G = np.zeros((n,n))
        for j in range(n):
            for k in range(j+1,n):
                temp = 1 - random.random()
                G[j][k] = temp
                G[k][j] = temp
        
        f = open("%s_%s.txt" % (n,i) ,"w")
        for j in range(n):
            for k in range(n-1):
                f.write(str(G[j][k]))
                f.write(" ")
            f.write(str(G[j][n-1]))
            f.write("\n")
