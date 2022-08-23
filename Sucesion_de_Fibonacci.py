# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 23:52:29 2022

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

def Sucesion_Fibonnaci_G(x):
    
    sf=[0,1]
    
    i=0
    j=1
    while len(sf)<=x:
        n=sf[i]+sf[j]
        sf.append(n)
        i+=1
        j+=1
        
    return sf

def Grafica_Sucesion_Fibonnaci(x):
    R=plt.plot(Sucesion_Fibonnaci_G(x),"r")
    plt.title("Fibonacci")
    plt.legend(("Serie Fibonacci",)
               ,prop={"size":13},loc="upper left")
        
    return R

plt.show(Grafica_Sucesion_Fibonnaci(20))




SF = Sucesion_Fibonnaci(100)

Razon  = SF[99] / SF[98]
print("Una estimacion del numero"
    +" aureo que nos da el dividir el termino 100 sobre el"
        +" 99 es: "+ str(Razon))



def Numero_Aureo(x):
    
    sf = Sucesion_Fibonnaci(x+1)
    i=0
    j=1
    eje_y=[]
    while j < x+1:
        razon= sf[j]/sf[i]
        eje_y.append(razon)
        i+=1
        j+=1
        
    return eje_y

print("Las primeras 5 aproximaciones que nos da la serie son: "
      +str(Numero_Aureo(5)))
    

def Numero_Aureo_G(x):
    eje_y = Numero_Aureo(x)
    aureo=[1.618033989]*19
    R = plt.plot(eje_y,"b",aureo,"r_")
    plt.title("Aproximacio al numero aureo")
    plt.legend(("Estimacion usando la serie","Numero Aureo")
               ,prop={"size":13},loc="upper right")
    
    return R

plt.show(Numero_Aureo_G(19))