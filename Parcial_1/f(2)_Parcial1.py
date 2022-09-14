# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 12:08:07 2022

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

def D_Central(f,x,h):
    
    Numerador = func(x+h) - func(x-h) 
    Denominador = 2*h
    R = Numerador / Denominador
    return R

y = D_Central(func,x,h) 

#plt.plot(x,y)


def derivT(X):
    Nume = (1/np.cos(x)) **2
    tan= np.tan(x)
    tansqr = (tan)**(1/2)
    deno =  2 *  tansqr
    R = Nume / deno
    return R

yt = derivT(x)

DPT = abs(yt - y)


plt.plot(x,DPT)
#plt.plot(x,yt)
