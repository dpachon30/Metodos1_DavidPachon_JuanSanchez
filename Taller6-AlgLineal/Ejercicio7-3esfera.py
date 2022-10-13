#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 18:45:18 2022

@author: juanpablo
"""

import numpy as np
import matplotlib.pyplot as plt

def F(r):
    return r[0]**2+r[1]**2+r[2]**2+r[3]**2-1
G = (F,)

def GetVectorF(G,r):
    v = G[0](r)
    return np.array([v])

def GetMetric(G,r):
    v = GetVectorF(G,r)
    return np.linalg.norm(v)

def GetJacobian(G,r,h=1e-6):
    dimen = len(G)
    J = np.zeros((dimen,4))
    
    for i in range(dimen):
        for j in range(4):
            aux = np.zeros(4)
            aux[j] = h
            J[i,j] = (  G[i](r+aux) - G[i](r-aux) )/(2*h)
        
    return J.T

def Coordenada(Min=-1,Max=1):
    p = [np.random.uniform(Min,Max),np.random.uniform(Min,Max),np.random.uniform(Min,Max),np.random.uniform(Min,Max)]
    return p

def GetSolve(G,r,lr=1e-3,epochs=int(1e5),error=1e-7):
    
    d = 1
    it = 0
    Vector_F = np.array([])
    R_vector = np.array(r)
    
    while d > error and it < epochs:
        CurrentF = GetMetric(G,r)
        J = GetJacobian(G,r)
        GVector = GetVectorF(G,r)

        #Machine Learning
        r -= lr*np.dot(J,GVector) 
        R_vector = np.vstack((R_vector,r))
        NewF = GetMetric(G,r)
        
        Vector_F = np.append(Vector_F,NewF)
        d = np.abs( CurrentF - NewF )/NewF
        it += 1
        

        
    if it == epochs:
        print(' Entrenamiento no completado ')
        
    return r,it,Vector_F,R_vector


n = 1e3
points = np.zeros((int(n),4))

for i in range(int(n)):
    sol,it,vect,rvect=GetSolve(G,Coordenada())
    points[i,0]= sol[0]
    points[i,1]= sol[1]
    points[i,2]= sol[2]
    points[i,3]= sol[3]
    
    
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(1,1,1, projection = '3d')

ax.set_xlim3d(-1, 1)
ax.set_ylim3d(-1, 1)
ax.set_zlim3d(-1, 1)

ax.view_init(10, 60)
X=points[:,0]
Y=points[:,1]
Z=points[:,2]
ax.scatter(X,Y,Z)
plt.show()