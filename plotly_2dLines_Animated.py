# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 13:27:04 2018

@author: jan.adamczyk
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

plt.ion()
plt.show()

x = np.linspace(0.,np.pi*4.,100)
ax.set_xlim([0.,13.])
ax.set_ylim([-1.5,1.5])
ax.set_zlim([-1.5,1.5])
for i in x:
    ax.scatter(i, np.sin(i), np.cos(i))
    print(i)
    plt.pause(0.01)