# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 20:58:48 2017

@author: arellave
"""

from sklearn.datasets import make_blobs
blobs,classes = make_blobs(500, centers=3)

import matplotlib.pyplot as plt
import numpy as np

'''
f,ax = plt.subplots(figsize=(7.5,7.5))
rgb=np.array(['r','g','b'])
ax.scatter(blobs[:,0],blobs[:,1],color = rgb[classes])
ax.set_title("Blobs")
'''

from sklearn.cluster import KMeans
kmean = KMeans(n_clusters=3)
kmean.fit(blobs)
print (kmean.cluster_centers_)

'''
f,ax = plt.subplots(figsize=(7.5,7.5))
rgb=np.array(['r','g','b'])
ax.scatter(blobs[:,0],blobs[:,1],color = rgb[classes])
ax.scatter(kmean.cluster_centers_[:,0],
           kmean.cluster_centers_[:,1],
            marker="*",
            s=250,
            color='black',
            label='Centers')
ax.set_title("Blobs")
ax.legend(loc='best')
'''

#print (the label of predicted class and original class
print (kmean.labels_[:5])
print (classes[:5])
#distance to 3 centers
print (kmean.transform(blobs)[:5])


#finding number of centroids
from sklearn import metrics
silhouette_samples = metrics.silhouette_samples(blobs,kmean.labels_)
print (np.column_stack((classes[:5],silhouette_samples[:5])))

'''
f,ax = plt.subplots(figsize=(10,5))
ax.set_title("Hist of Silhouette Samples")
ax.hist(silhouette_samples)
'''

print (silhouette_samples.mean())
print (metrics.silhouette_score(blobs,kmean.labels_))


blobs,classes = make_blobs(500,centers=10)
sillhouette_avgs = []


for k in range(2,60):
    kmean = KMeans(n_clusters=k).fit(blobs)
    sillhouette_avgs.append(metrics.silhouette_score(blobs,kmean.labels_))

f,ax = plt.subplots(figsize=(7,5))
ax.plot(sillhouette_avgs)



