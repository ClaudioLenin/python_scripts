# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 15:35:45 2022

@author: PC HP
"""

import numpy as np
import matplotlib.pyplot as plt

N=50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = np.pi*(15*np.random.rand(N))**2 #0 to 15 point radii

plt.scatter(x, y, s = area,c = colors,alpha = 0.5)
plt.show()