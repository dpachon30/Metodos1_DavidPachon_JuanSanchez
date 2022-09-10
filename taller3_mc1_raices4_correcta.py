# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 09:16:33 2022

@author: ACER
"""

import numpy as np
import sympy as sym
import matplotlib.pyplot as plt



x = np.arange(-1,1,0.01)
legendre = [x, (3*x**2 - 1)/2]
#abc = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t]
    
    
def Function(x):
    a = x   
    return a


#x = np.arange(-1,1,0.1)
y = Function(x)
plt.axhline(y=0,color='r')
plt.plot(x,y)

#print(len(y))

""

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



""

def GetAllRoots(x,tolerancia=1):
    
    Roots = np.array([])
    
    for i in x:
        root = GetNewtonMethod(Function,Derivative,i)
        if (abs(root)+1.0e-07) < 1.0e-06:
            #root = round(root,5)
            if root != False:
                
                croot = abs(round(root,13))
                
                if croot not in Roots:
                    Roots = np.append(Roots, croot)
            
        
        elif (abs(root)+1.0e-06) > 1.0e-05:
            root = round(root,2)
            if root != False:
                
                croot = root
                
                if croot not in Roots:
                    Roots = np.append(Roots, croot)
                
                
                 
    Roots.sort()
    
    return Roots

print(GetAllRoots(x))

def Function(x):    
    b = (3*x**2 - 1)/2    
    return b

print(GetAllRoots(x))


def Function(x):    
    c = x*(5*x**2 - 3)/2    
    return c
print(GetAllRoots(x))

def Function(x):    
    d = (8*x**4 + 24*x**2*(x**2 - 1) + 3*(x**2 - 1)**2)/8
    
    return d
print(GetAllRoots(x))


def Function(x):
    
    e = x*(8*x**4 + 40*x**2*(x**2 - 1) + 15*(x**2 - 1)**2)/8
    
    return e
print(GetAllRoots(x))

def Function(x):
    
    f = (16*x**6 + 120*x**4*(x**2 - 1) + 90*x**2*(x**2 - 1)**2 + 5*(x**2 - 1)**3)/16
    
    return f
print(GetAllRoots(x))

def Function(x):
    g = x*(16*x**6 + 168*x**4*(x**2 - 1) + 210*x**2*(x**2 - 1)**2 + 35*(x**2 - 1)**3)/16
    
    return g
print(GetAllRoots(x))

def Function(x):
    h = (128*x**8 + 1792*x**6*(x**2 - 1) + 3360*x**4*(x**2 - 1)**2 + 1120*x**2*(x**2 - 1)**3 + 35*(x**2 - 1)**4)/128
    
    return h
print(GetAllRoots(x))


def Function(x):
    i = x*(128*x**8 + 2304*x**6*(x**2 - 1) + 6048*x**4*(x**2 - 1)**2 + 3360*x**2*(x**2 - 1)**3 + 315*(x**2 - 1)**4)/128
    
    return i
print(GetAllRoots(x))

def Function(x):
    j = (256*x**10 + 5760*x**8*(x**2 - 1) + 20160*x**6*(x**2 - 1)**2 + 16800*x**4*(x**2 - 1)**3 + 3150*x**2*(x**2 - 1)**4 + 63*(x**2 - 1)**5)/256
    
    return j
print(GetAllRoots(x))

def Function(x):
    k = x*(256*x**10 + 7040*x**8*(x**2 - 1) + 31680*x**6*(x**2 - 1)**2 + 36960*x**4*(x**2 - 1)**3 + 11550*x**2*(x**2 - 1)**4 + 693*(x**2 - 1)**5)/256
    return k
print(GetAllRoots(x))


def Function(x):
    l = (1024*x**12 + 33792*x**10*(x**2 - 1) + 190080*x**8*(x**2 - 1)**2 + 295680*x**6*(x**2 - 1)**3 + 138600*x**4*(x**2 - 1)**4 + 16632*x**2*(x**2 - 1)**5 + 231*(x**2 - 1)**6)/1024
    
    return l
print(GetAllRoots(x))

def Function(x):
    m = x*(1024*x**12 + 39936*x**10*(x**2 - 1) + 274560*x**8*(x**2 - 1)**2 + 549120*x**6*(x**2 - 1)**3 + 360360*x**4*(x**2 - 1)**4 + 72072*x**2*(x**2 - 1)**5 + 3003*(x**2 - 1)**6)/1024
    
    return m
print(GetAllRoots(x))

def Function(x):
    n = (2048*x**14 + 93184*x**12*(x**2 - 1) + 768768*x**10*(x**2 - 1)**2 + 1921920*x**8*(x**2 - 1)**3 + 1681680*x**6*(x**2 - 1)**4 + 504504*x**4*(x**2 - 1)**5 + 42042*x**2*(x**2 - 1)**6 + 429*(x**2 - 1)**7)/2048
    
    return n
print(GetAllRoots(x))


def Function(x):
    o = x*(2048*x**14 + 107520*x**12*(x**2 - 1) + 1048320*x**10*(x**2 - 1)**2 + 3203200*x**8*(x**2 - 1)**3 + 3603600*x**6*(x**2 - 1)**4 + 1513512*x**4*(x**2 - 1)**5 + 210210*x**2*(x**2 - 1)**6 + 6435*(x**2 - 1)**7)/2048
    
    return o
print(GetAllRoots(x))

def Function(x):
    p = (32768*x**16 + 1966080*x**14*(x**2 - 1) + 22364160*x**12*(x**2 - 1)**2 + 82001920*x**10*(x**2 - 1)**3 + 115315200*x**8*(x**2 - 1)**4 + 64576512*x**6*(x**2 - 1)**5 + 13453440*x**4*(x**2 - 1)**6 + 823680*x**2*(x**2 - 1)**7 + 6435*(x**2 - 1)**8)/32768
    
    return p
print(GetAllRoots(x))

def Function(x):
    q = x*(32768*x**16 + 2228224*x**14*(x**2 - 1) + 29245440*x**12*(x**2 - 1)**2 + 126730240*x**10*(x**2 - 1)**3 + 217817600*x**8*(x**2 - 1)**4 + 156828672*x**6*(x**2 - 1)**5 + 45741696*x**4*(x**2 - 1)**6 + 4667520*x**2*(x**2 - 1)**7 + 109395*(x**2 - 1)**8)/32768
    
    return q
print(GetAllRoots(x))

def Function(x):
    r = (65536*x**18 + 5013504*x**16*(x**2 - 1) + 75202560*x**14*(x**2 - 1)**2 + 380190720*x**12*(x**2 - 1)**3 + 784143360*x**10*(x**2 - 1)**4 + 705729024*x**8*(x**2 - 1)**5 + 274450176*x**6*(x**2 - 1)**6 + 42007680*x**4*(x**2 - 1)**7 + 1969110*x**2*(x**2 - 1)**8 + 12155*(x**2 - 1)**9)/65536
    
    return r
print(GetAllRoots(x))


def Function(x):
    s = x*(65536*x**18 + 5603328*x**16*(x**2 - 1) + 95256576*x**14*(x**2 - 1)**2 + 555663360*x**12*(x**2 - 1)**3 + 1354429440*x**10*(x**2 - 1)**4 + 1489872384*x**8*(x**2 - 1)**5 + 744936192*x**6*(x**2 - 1)**6 + 159629184*x**4*(x**2 - 1)**7 + 12471030*x**2*(x**2 - 1)**8 + 230945*(x**2 - 1)**9)/65536
    
    return s
print(GetAllRoots(x))

def Function(x):
    t = (262144*x**20 + 24903680*x**18*(x**2 - 1) + 476282880*x**16*(x**2 - 1)**2 + 3175219200*x**14*(x**2 - 1)**3 + 9029529600*x**12*(x**2 - 1)**4 + 11918979072*x**10*(x**2 - 1)**5 + 7449361920*x**8*(x**2 - 1)**6 + 2128389120*x**6*(x**2 - 1)**7 + 249420600*x**4*(x**2 - 1)**8 + 9237800*x**2*(x**2 - 1)**9 + 46189*(x**2 - 1)**10)/262144
    
    return t
print(GetAllRoots(x))




#abc = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t]













