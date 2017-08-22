# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 19:30:39 2017

@author: arellave
"""

#Loading data using std library

import csv
import numpy
filename = 'pima-indians-diabetes.data.csv'
raw_data = open(filename,'rt')
reader = csv.reader(raw_data,delimiter=',', quoting=csv.QUOTE_NONE)
x = list(reader)
data = numpy.array(x).astype('float')
print(data.shape)


#loading using Numpy
raw_data = open(filename,'rt')
data1 = numpy.loadtxt(raw_data,delimiter=",")
print(data1.shape)

#loading using url
import urllib
url="https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
raw_data = urllib.urlopen(url)
dataset = numpy.loadtxt(raw_data,delimiter = ",")
print(dataset.shape)


#Loading using pandas
import pandas
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pandas.read_csv(filename,names=names)
print(data.shape)

#Loading from url
data = pandas.read_csv(url,names=names)
print(data.shape)
