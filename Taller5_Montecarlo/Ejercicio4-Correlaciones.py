# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 16:43:03 2022

@author: ACER
"""

import numpy as np
import matplotlib.pyplot as plt

N = 10000
K = 1
RK = []
lista = np.random.rand(N+K)
while K<=30:
    #lista = np.random.rand(N+K)
    #lista = np.random.rand(5+K) 
    
    A = 0
    
    largo_lista= len(lista)-K
    ll =largo_lista 
    for i in range(ll):
        A += lista[i]*lista[i+K]
        
    r = A/ll
    RK.append(r) 
    K+=1

print(len(RK)) 
x = np.arange(1,31,1)
plt.plot(x,RK)
plt.axhline(y=0.28,color="r")
plt.axhline(y=0.25,color="r")
plt.axhline(y=0.22,color="r")
plt.grid()