# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 15:46:57 2017

@author: arellave
"""

from random import randint
import numpy as np
import matplotlib.pyplot as plt

n = 400  # random walk length
N = 10000 # number of repeated walks

reps = np.empty(N)

for i in range(N):
    random_walk = [2*randint(0, 1) - 1 for _ in range(n)]
    reps[i] = abs(sum(random_walk)) / n
    
plt.hist(reps, bins=41)
plt.xlabel("$|S_n|/n$")
plt.show()