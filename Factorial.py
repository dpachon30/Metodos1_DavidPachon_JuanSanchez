# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 19:15:41 2022

@author: ACER
"""


def factorial_de_Natural(x:int)->int:
    contador=0
    R=x
    
    if x==1 or x==0:
        R=1
    else:
        while contador < x:
            R*= (x-1)
            contador=+1
            x-=1
        
    return R 

print("Primeros 20 factoriales:")    
P20NF = []
for i in range(1,21):
    f = factorial_de_Natural(i-1)
    P20NF.append(f)
    
print(P20NF)    
#print(len(P20NF))
    

def variaciones_sin_repeticion(x:int,y:int)->float:
    numerador= factorial_de_Natural(x)
    denominador= factorial_de_Natural(x-y)
    
    R= numerador/ denominador
    return R
    
print("2.  6 carros en 3 estacionamientos se pueden ubicar de: "
     + str(variaciones_sin_repeticion(6,3))+" maneras")   


def combinaciones_sin_repeticion(x:int,y:int)->float:
    
    numerador= factorial_de_Natural(x)
    denominador= factorial_de_Natural(y) * factorial_de_Natural(x-y)
    
    R= numerador/denominador
    
    return R

print("3.")
print("Cualquiera puede ser el arquero: "
      + str(combinaciones_sin_repeticion( 22,11 ))) 

print("Ya sabemos quien sera el arquero: "
      + str(combinaciones_sin_repeticion( 21,10 )))

