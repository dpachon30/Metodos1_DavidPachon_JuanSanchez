#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 16:37:55 2022

@author: juanpablo
"""

import numpy as np

import sympy as sym

import matplotlib.pyplot as plt

def PolinomiosLaguerre(n):
    
    x = sym.Symbol('x',Real=True)
    y = sym.Symbol('y',Real=True)
    
    y = ((np.e**-x*x**n))
    
    p = sym.diff(y,x,n)*(np.e**x/(np.math.factorial(n)))
    
    return p

#Funcion destinada a hallar una raiz

def GetNewtonMethod(f,df,xn,itmax = 100000, precision=1e-12):
    
    error = 1.
    it = 0
    
    while error > precision and it < itmax:
        
        try:
            
            xn1 = xn - f(xn)/df(xn)
            
           
            error = np.abs(f(xn)/df(xn))
        
        except ZeroDivisionError:
            print("zero division")
            
        xn  = xn1
        it += 1
    
    #print('Raiz:',xn,it)
    
    if it == itmax:
        return False
    else:
        return xn

#Funcion destinada a hallar las raices del polinomio

def GetAllRoots(f,df,x, tolerancia=9):
    
    Roots = np.array([])
    
    for i in x:
        
        root = GetNewtonMethod(f,df,i)
          
        if root != False:
            
            croot = np.round( root, tolerancia ) 
            
            if croot not in Roots:
                Roots = np.append( Roots, croot )
                
    # Ordenamos las raices
    Roots.sort()
    
    return Roots

def GetRootsPolynomial(xi,poly,dpoly):

    
    x = sym.Symbol('x',Real=True)
    
    pn = sym.lambdify([x],poly,'numpy')
    dpn = sym.lambdify([x],dpoly,'numpy')
    Roots = GetAllRoots(pn,dpn,xi,tolerancia=8)
    
    return Roots
    

#Funcion destinada a hallar los pesos

def WeightsLaguerre(puntos):
    
    xi=np.linspace(0,100,1000)
    
    x = sym.Symbol('x',Real=True)
    
    weights= []
    
    ln=PolinomiosLaguerre(puntos+1)
    
    ln2=PolinomiosLaguerre(puntos)
    
    lnx = sym.lambdify([x],ln2,'numpy')
        
    dln=sym.diff(ln,x)
    
    
    xi=np.linspace(0,100,1000)
    
    raices= GetRootsPolynomial(xi, ln, dln)
    
    
    
    for i in raices:
        
       
        
        wk= i/((puntos+1)**2 * (lnx(i)**2))
        
        
        
        weights.append(wk)
        
        
    return weights

#Funcion para la integral

def GausLaguerre(f,points):
    
    
    x = sym.Symbol('x',Real=True)
    
    xi=np.linspace(0,100,1000)
                    
    pesos=WeightsLaguerre(points)
    
        
    f=sym.lambdify([x],f,'numpy')
    
    integral=0

    
    funl=PolinomiosLaguerre(points+1)
    
    dfunl=sym.diff(funl,x)
    
    raices= GetRootsPolynomial(xi,funl,dfunl)
    
        
    for i in range(len(pesos)):
                       
        xn=pesos[i]*(f(raices[i]))
        
        integral += xn
        
    return integral

  
#Se define la funcion del enunciado

x = sym.Symbol('x',Real=True)
f= ((x**3)/(np.e**x - 1))* np.e**(x)

#Ejecucion

res= GausLaguerre(f,3)

print(res)




#Gráfica de error de la derivada en n puntos

p=11
valores=[]
puntoss=[]
for i in range(1,p):
    
    derivada=GausLaguerre(f,i)
    error=derivada/((np.pi**4)/15)
    puntoss.append(i)
    valores.append(error)
    

plt.scatter(puntoss,valores,color='r')

plt.show() 
    