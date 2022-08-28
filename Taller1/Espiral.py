# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 19:00:40 2022

@author: ACER
"""


import numpy as np
from matplotlib import pyplot as plt


t= np.linspace(0,2*np.pi)

a=1
b=0
r = b + a*t

plt.figure().add_subplot(111, projection="polar").plot(t,r)
plt.show()