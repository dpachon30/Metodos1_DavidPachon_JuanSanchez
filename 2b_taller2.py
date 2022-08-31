# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 22:34:41 2022

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



def DerivativeC3(x,f,h):
    return (f(x+2*h)-(3*f(x+h))+(3*f(x))-f(x-h))/(h**3)  

def calcular_el_error(x,f,h):
    R = ((h**2)/3) * DerivativeC3(x,f,h)
    return R    

print(calcular_el_error(x,f,h)) 
