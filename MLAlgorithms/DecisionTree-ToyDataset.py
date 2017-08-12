# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 20:39:41 2017

@author: arellave
"""
#%%

from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
X = [[0,0],[1,1],[0,1]]
Y = [0,1,0]

classifier = tree.DecisionTreeClassifier(random_state=0, criterion = 'entropy',max_depth=None)
classifier.fit(X,Y)


print(classifier.predict([[2,2]]))
tree.export_graphviz(classifier)

classifier2 = RandomForestClassifier(n_estimators=10, random_state = 0, criterion='entropy',max_depth=None)
classifier2.fit(X,Y)
print(classifier2.predict([[2,2]]))

#%%
