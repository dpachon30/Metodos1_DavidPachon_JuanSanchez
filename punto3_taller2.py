# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 21:26:55 2022

@author: ACER
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import sympy as sym


x = sym.Symbol('x',Real=True)

func = 1/(1+sym.exp(-x**2))**(1/2)
f= sym.lambdify([x],func,'numpy')


x = np.linspace(-10,10,402)
y = f(x)
plt.plot(x,y)

h  = 0.05

#print(y)
#print(y[9])
M = [1,0,-1] 

M = [-1,0,1 ]   
"forma correcta"

  



def convolucion_discreta(y):
    puntos=[0]
    c1 = 0
    c3 = 2
    while (c1+3) <= len(y): 
        
        
        vu1= y[c1]
        vu3= y[c3]
        vpd = -vu1 + vu3
        vpd = vpd *  (1/(2*h))
        
        puntos.append(vpd) 

        c1 +=1
        c3 +=1
    puntos.append(0)    
    return puntos

Dy = convolucion_discreta(y)
plt.plot(x,Dy)

print(Dy)  

       
