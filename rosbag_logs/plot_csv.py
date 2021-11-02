#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 00:27:21 2021

@author: tor
"""

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd


plt.style.use('seaborn')
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

def animation(i):
  AAPL_STOCK = pd.read_csv('radar_scan_test.csv')
  x = []
  y = []
  x = AAPL_STOCK[0:i]['.x']
  y = AAPL_STOCK[0:i]['.y']
  print(i)
  
  ax.clear()
  ax.scatter(x, y)
  
  
animation = FuncAnimation(fig, func=animation, interval=1)
plt.show()
