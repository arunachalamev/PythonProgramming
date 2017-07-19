# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 15:48:07 2017

@author: arellave
"""
#%%
inputFile = r'C:\Users\arellave\Desktop\Header.txt'
dataFile = r'C:\Users\arellave\Desktop\Data.txt'
#Slice = r"FlightID;SiteLink;Twitter;Smart"
#Slice = Slice.split(";")
Slice = ['FlightID','Slice']
Label = r'Label'
Score = r'Score'

import pandas as pd
from pandas import DataFrame

df = DataFrame.from_csv(inputFile, sep="\t", index_col=None, header = None)

#reade the columnHeader and Flattening
columnHeader = [line.split('\t') for line in open(inputFile, 'r')]
columnHeader = [val for sublist in columnHeader for val in sublist]

#print (columnHeader)

#Reading data file
data = DataFrame.from_csv(dataFile, sep="\t", index_col=None, header = None)
#print data

#Setting the column header
data.columns  = columnHeader
#print data
#print data['Label']

for SliceDimension in Slice:
    unique = data[SliceDimension].unique()
#    print unique

    #Calculating AUC
    from sklearn.metrics import roc_auc_score
    
    for i in unique:
        newData = data[data[SliceDimension]==i]
#        print newData
        val = roc_auc_score(newData[Label], newData[Score])
        print "Slice=",SliceDimension, "Value=", i, "AUC=",val 
    

#uniqueValue = list(set(data['Slice']))

#Calculating AUC
#from sklearn.metrics import roc_auc_score
#val = roc_auc_score(data['Label'], data['Score'])
#print val

#%%

Slice = r"FlightID;SiteLink;Twitter;Smart"
text  = Slice.split(";")
print text

#%%