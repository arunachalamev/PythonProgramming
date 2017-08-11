# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 20:39:41 2017

@author: arellave
"""
#%%

from sklearn import tree
X = [[0,0],[1,1],[0,1]]
Y = [0,1,0]

classifier = tree.DecisionTreeClassifier(random_state=0, criterion = 'entropy',max_depth=None)
classifier.fit(X,Y)


print(classifier.predict([[0,3]]))

tree.export_graphviz(classifier)

#%%
