# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 20:58:53 2017

@author: arellave
"""


import scipy.spatial.distance as dist
import numpy as np

# Prepare 2 vectors (data points) of 10 dimensions
A = np.random.uniform(0, 10, 10)
B = np.random.uniform(0, 10, 10)

print A
print B

# Perform distance measurements 
print '\nEuclidean distance is', dist.euclidean(A, B)
print 'Manhattan distance is', dist.cityblock(A, B)
print 'Chebyshev distance is', dist.chebyshev(A, B)
print 'Canberra distance is', dist.canberra(A, B)
print 'Cosine distance is', dist.cosine(A, B)

# Prepare 2 vectors of 100 dimensions
AA = np.random.uniform(0, 10, 100)
BB = np.random.uniform(0, 10, 100)

# Perform distance measurements
print '\nEuclidean distance is', dist.euclidean(AA, BB)
print 'Manhattan distance is', dist.cityblock(AA, BB)
print 'Chebyshev distance is', dist.chebyshev(AA, BB)
print 'Canberra distance is', dist.canberra(AA, BB)
print 'Cosine distance is', dist.cosine(AA, BB)

