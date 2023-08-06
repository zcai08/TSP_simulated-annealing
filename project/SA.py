import numpy as np
import matplotlib.pyplot as plt
import os
from python_tsp.exact import solve_tsp_dynamic_programming
import time
def TSP_SA(G):
    s = list(range(len(G)))
    c = cost(G, s)
    ntrial = 1
    T = 4000
    alpha = 0.99
    while ntrial <= 1000:
      n = np.random.randint(0, len(G))
      m = np.random.randint(0, len(G))
      if n == m:
        break
      s1 = swap(s, m, n)
      c1 = cost(G, s1)
      if c1 < c:
        s, c = s1, c1
      else:
        if np.random.rand() < np.exp(-(c1 - c)/T):
          s, c = s1, c1
      T = alpha*T
      ntrial += 1
    return s,c
    

def swap(s, m, n):
    i, j = min(m, n), max(m, n)
    s1 = s.copy()
    while i < j:
      s1[i], s1[j] = s1[j], s1[i]
      i += 1
      j -= 1
    return s1
  
def cost(G, s):
    l = 0
    for i in range(len(s)-1):
      l += float(G[s[i]][s[i+1]])
    l += float(G[s[len(s)-1]][s[0]]) 
    return l

def mini_tree(G):
    visited = []
    l = 0
    visited.append(0)
    while len(visited) < G.shape[0]:
        min_weight = 1
        v1 = 0
        v2 = 0
        for v in visited:
            for i in range(G.shape[0]):
                if i not in visited and float(G[v][i]) < min_weight:
                    v2 = v
                    v1 = i
                    min_weight = float(G[v][i])
        visited.append(v1)
        l += float(G[v2][v1])
    return l

if __name__ == "__main__" :
    d = 'E:\\project'
    Y = []
    Z = np.zeros(8)
    for file in os.listdir(d):
        G = []
        if not file.endswith('.txt'):
            continue
        with open(file, 'r') as f:
            for line in f.readlines():
                G.append(line.split(' '))
        print(file)
        t1 = time.time()
        temp_s, temp_c = TSP_SA(G)
        t2 = time.time()
        print(temp_s)
        print(temp_c)
        print(t2-t1)
        G = np.array(G)
        ###print(mini_tree(G))
        if file.startswith('10_'):
            Z[0] += temp_c ### - mini_tree(G)
            Z[4] += float(t2 - t1)
        elif file.startswith('100_'):
            Z[1] += temp_c ### - mini_tree(G)
            Z[5] += float(t2 - t1)
        elif file.startswith('1000_'):
            Z[2] += temp_c ### - mini_tree(G)
            Z[6] += float(t2 - t1)
        elif file.startswith('10000_'):
            Z[3] += temp_c ### - mini_tree(G)
            Z[7] += float(t2 - t1)
    for i in range(8):
        Z[i] = Z[i]/10
    plt.xscale("log")
    plt.plot([10,100,1000,10000],Z[0:4])
    plt.show()
    
    plt.xscale("log")
    plt.plot([10,100,1000,10000],Z[4:8])
    plt.show()
    

