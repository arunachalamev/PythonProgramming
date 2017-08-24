# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 20:35:25 2017

@author: arellave
"""

from numpy import linalg
U,Sigma,VT = linalg.svd([[1,1],[7,7]])

print U,"\n",Sigma,"\n",VT


Data = [[1,1,1,0,0],
        [2,2,2,0,0],
        [1,1,1,0,0],
        [5,5,5,0,0],
        [1,1,0,2,2],
        [0,0,0,3,3],
        [0,0,0,1,1]]
        
U,Sigma,VT = linalg.svd(Data)
#print Data
print Sigma

Sig3 = mat([[Sigma[0],0,0],
           [0,Sigma[1],0],
            [0,0,Sigma[2]]])

U[:,:3]*Sig3*VT[:3,:]