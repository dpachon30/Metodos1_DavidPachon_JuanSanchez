# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 20:16:37 2022

@author: ACER
"""

from matplotlib import pyplot as plt


def Sucesion_Fibonnaci(x):
    
    sf=[0,1]
    
    i=0
    j=1
    while len(sf)<=x:
        n=sf[i]+sf[j]
        sf.append(n)
        i+=1
        j+=1
    R=sf[1:x+1]    
    return R

print("Primeros 20 terminos de la sucesion de Fibonacci: ")    
print(Sucesion_Fibonnaci(20))
