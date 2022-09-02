# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 21:50:00 2022

@author: ACER
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import sympy as sym


CP = 400

x = sym.Symbol('x',Real=True)
eax = sym.exp(-x**2)
func = (x*sym.exp(-x**2)) / (1+sym.exp(-x**2))**(3/2)
f= sym.lambdify([x],func,'numpy')

x = np.linspace(-10,10,CP)
yt = f(x)

#grafica derivada teorica
#plt.plot(x,yt)

h  = 0.05



x = sym.Symbol('x',Real=True)
func = 1/(1+sym.exp(-x**2))**(1/2)
f= sym.lambdify([x],func,'numpy')

x = np.linspace(-10,10,CP)
y = f(x)


 

def DerivativeC(x,f,h):
    return (f(x+h)-f(x-h))/(2*h)

DerivadaC = DerivativeC(x,f,h)





y_error = abs(DerivadaC - yt)
#print(DerivadaC,yt,y_error)
plt.plot(x,y_error,"y") 


"""

 "Forma alternativa(al abs()):"
 
 
r = []

for i in range(len(yt)):
    
    if yt[i]<=DerivadaC[i]:
        a=DerivadaC[i] - yt[i]
        r.append(a)
        
    elif yt[i]>=DerivadaC[i]:
        a=  yt[i] - DerivadaC[i] 
        r.append(a)    
        
    else:
        r.append(yt[i])

print(len(r))
plt.plot(x,r,"b")            
            
"""    