# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 20:34:06 2022

@author: ACER
"""

import numpy as np
from matplotlib import pyplot as plt


def numero_primo(x:int)->bool:
    R=True
    for i in range(2,x):
        
        if x%i == 0:
            R=False
            
    return R

def primeros_numeros_primos(x)->list:

    R=[]
    i=2
    while len(R)<x:
        c=numero_primo(i)
        if c == True:       
        
            R.append(i)
            i +=1
        else:
            i+=1
    
    return R
 
P_1000_NP = primeros_numeros_primos(1000)
#P_10_NP = P_1000_NP[0:10] 
#print(P_10_NP)
    
