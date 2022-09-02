# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 16:56:14 2022

@author: ACER
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import sympy as sym


x = sym.Symbol('x',Real=True)
func = 1/(1+sym.exp(-x**2))**(1/2)
f= sym.lambdify([x],func,'numpy')

x = np.linspace(-10,10,4000)
y = f(x)

#grafica de la funcion en la linea de abajo
#plt.plot(x,y)


# 20 / 0.05 = 400

h  = 0.05

 

def DerivativeC(x,f,h):
    return (f(x+h)-f(x-h))/(2*h)

DerivadaC = DerivativeC(x,f,h)

plt.plot(x,DerivadaC,"orange")


