#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 23:25:15 2022
@author: ACER
"""

import numpy as np
import matplotlib.pyplot as plt

X = [1.4,3.5,5.6]
Y = [0.4007954931819738,0.594128102489774,0.29802795523938164]

def Lagrange(x,xi,j):
    
    prod = 1.0
    n = len(xi)
    
    for i in range(n):
        if i != j:
            prod *= (x - xi[i])/(xi[j]-xi[i])
            
    return prod
def Poly(x,xi,yi):
    
    Sum = 0.
    n = len(xi)
        
    for j in range(n):
        Sum += yi[j]*Lagrange(x,xi,j)
        
        
    return Sum

x = np.linspace(0,6.5,100)
y = Poly(x,X,Y)
plt.scatter(X,Y,color='r')
plt.plot(x,y,color='k')


#print(len(y),len(x))
#print(Poly(2,X,Y))

"""
# Se usa de aqui en adelante algebra para obtener teta y la
# magnitud de V0
# En base la formula: 
# Yf = tan(teta)Xf - (g/(2*cos^2(teta)*V0^2))Xf^2
# si Xf = 1
# Yf = bXf - aXf^2
# Donde a = g/(2*cos^2(teta)*V0^2  , b = tan(teta)
"""

xf = 2
yf = Poly(xf,X,Y)  

ff1 = Poly(1,X,Y)

b = (yf - ((xf**2)*ff1)) / (xf-(xf**2)) 

a = b - ff1 

angulo = np.arctan(b)
angulo_grados = (angulo * 180) / np.pi

g = 9.81
cosct = (np.cos(angulo))**2
V0SQR = g/(a*2*cosct)
V0 = V0SQR ** (1/2)

V0x = round(V0)  * np.cos(angulo)
V0y = round(V0)  * np.sin(angulo)

#print("b = ",b)
#print("a = ",a)  
print("El angulo es ",round(angulo,3),"radianes") 
print("El angulo es ",round(angulo_grados,2),"grados")
print("La magnitud de la velocidad inicia es:",round(V0),"m/s")
print("El vector es ",round(V0x,3),"i + ",round(V0y,3),"j")