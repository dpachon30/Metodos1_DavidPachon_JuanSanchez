# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 11:10:37 2022

@author: ACER
"""

import numpy as np
import matplotlib.pyplot as plt

#print(np.tan(0))

h = 0.001

x = np.arange(0.1,1.1,h)

def func(x):    
    a= np.tan(x)
    R = (a)**(1/2)
    return R

def progre_orden_2(f,x,h):
    
    Numerador = -3*f(x)  + 4*f(x+h) - f(x+(2*h))
    Denominador = 2*h
    R = Numerador / Denominador
    return R

y = progre_orden_2(func,x,h) 

plt.plot(x,y)




    
    
 