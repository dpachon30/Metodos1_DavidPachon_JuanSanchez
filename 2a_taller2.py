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

x = np.linspace(-10,10,400)
y = f(x)
plt.plot(x,y)


# 20 / 0.05 = 400


#x = np.linspace(-10,10,500)
h  = 0.05

 
def DerivativeR(x,f,h):
    return (f(x+h)-f(x))/h
def DerivativeL(x,f,h):
    return (f(x)-f(x-h))/h
def DerivativeC(x,f,h):
    return (f(x+h)-f(x-h))/(2*h)
DerivadaR = DerivativeR(x,f,h)
DerivadaL = DerivativeL(x,f,h)
DerivadaC = DerivativeC(x,f,h)

plt.plot(x,DerivadaC)


# calcular la derivada en 20 o en 400 puntos ?

x = np.linspace(-10,10,20)
DerivadaC = DerivativeC(x,f,h)
print(DerivadaC)
print(len(DerivadaC))


