# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 00:07:07 2022

@author: ACER
"""

import numpy as np
import sympy as sym
import matplotlib.pyplot as plt


def Function(x):
    return 3*(x**5) + 5*(x**4) - (x**3)


x = np.arange(-10,10,0.1)
y = Function(x)
plt.axhline(y=0,color='r')
plt.plot(x,y)

def Derivative(f,x,h=1e-6):
    return (f(x+h)-f(x-h))/(2*h)
#Derivative = 15*(x**4) + 20*(x**3) - 3*(x**2)


def GetNewtonMethod(f,df,xn,itmax=1000,precision=1e-5):
    
    error = 1
    it=0
    
    while error > precision and it < itmax:
        
        try:
            
            xn1 = xn - f(xn)/df(f,xn)
            error = np.abs(f(xn)/df(f,xn))
            
        except ZeroDivisionError:
            print('Division por cero')
            
        xn = xn1
        it += 1
        
    #print('raiz:', xn,it)
    
    if it == itmax:
        return False
    else:
        return xn
    
#root = GetNewtonMethod(Function,Derivative,6)

#print(root)





def GetAllRoots(x,tolerancia=1):
    
    Roots = np.array([])
    
    for i in x:
        root = GetNewtonMethod(Function,Derivative,i)
        if (abs(root)+1.0e-06) < 1.0e-05:
            
            if root != False:
                
                croot = abs(round(root,13))
                
                if croot not in Roots:
                    Roots = np.append(Roots, croot)
            
        
        elif (abs(root)+1.0e-06) > 1.0e-05:
            root = round(root,3)
            if root != False:
                
                croot = root
                
                if croot not in Roots:
                    Roots = np.append(Roots, croot)
                
                
                 
    Roots.sort()
    
    return Roots

print(GetAllRoots(x))

