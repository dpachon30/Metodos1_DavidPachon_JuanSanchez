# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 15:27:44 2022

@author: ACER
"""


import numpy as np
import matplotlib.pyplot as plt

a = 0
b = 1
n = 10  
h = (b-a)/n
x = np.arange(a+h,b,h)

def function(x):
    
    f = np.exp(-x**2)
    
    return f

y = function(x)
#print(len(x),len(y))
plt.plot(x,y)
    
s1 = (h/2)*(function(a)+function(b))
sumatoria = 0
for i in range(len(x)):
    sumando = function(x[i])*h
    sumatoria += sumando
    
R = s1 + sumatoria    

print("El valor de la integral es: ",round(R,5))




yd2 = (function(x+h) - 2*function(x) + function(x-h)) / h**2
#plt.plot(x,yd2) 
maximo = np.max(np.abs(yd2))
nomerror = ((h**2)*(b-a))*(1/12)
ERROR = nomerror * maximo 
#print(maximo)
print("El error esta acotado " 
      +"por el valor maximo promedio "
      +"que tome la segunda derivada: ",round(ERROR,7))

