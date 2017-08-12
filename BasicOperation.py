# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 08:21:09 2017

@author: arellave
"""
#%%
print(7/3)  #integer division
print(7.5/3)    #float division
print(3**2+2**3)    #exponential

from math import cos,exp,pi   #importing math function
print(cos(exp(-9)*pi)+4+5j)     

# variable declaration 
myvar = 3
myvar +=2
print (myvar)
myvar -=1
print(myvar)


""" String Object """
#string operation
#myvar=""
mystring ="Hello"
mystring += "world."
print(mystring)     #prints the string
print (mystring[2:6])   #prints the string from 2 position to 5th position excluding
print (mystring[2:-3])  #starts from position 2 and prints till last but 3

print('a %s parrot' % 'dead')

print [x for x in mystring]     # to access each character in string

'world' in mystring     # to find word presence

myvar, mystring = mystring, myvar #swaps integer and string



"""Tuple object"""
#tupe
a=(1,2,3)
a[1]
#a[1]=3 -> tuple object doesn't support item assignment


"""List object """
mylist = ["List Item",2,3.14] #List support heterogenous datatype
print mylist[:]
print mylist[1:2] # start at index 1 and till 2 exclusive

print mylist[-1:] #print last 1 item
print mylist[-3:-1] 

print mylist[1:]

mylist.extend([4,5,6])  #extends an iterable object
mylist.append(7)    #append an item
#mylist.append([8]) -> this differs from above statement

print mylist
print mylist[::2]   # skips element at position multiples of 2


mylist[0]=8     # list is an mutable object

mylist.sort()
mylist.reverse()
mylist.index(3.14)

del mylist[2:4]
mylist[1:2]=[4.5,2.3]
[x for x in range(2,23,3)]

[x for x in range(2,23,3) if x%2 ==1]

[x*y for x in [1,2,3] for y in [3,4,5]]

any([i%3 for i in [3,3,4,4,3]])
sum(1 for i in [3,3,4,4,3] if i ==4)


L1=[1,('a',3)]
L2=[1,('a',3)]
print L1 == L2      # checks for value equality
print L1 is L2      # checks object referencing same address


"""Dictionary Object"""
d1={}
d2={'spam':2,'eggs':3}
d3 ={'food':{'ham':1,"eggs":2}}

d2['eggs']
d3['food']['ham']

'eggs' in d2
d2.keys()
d2.values()
len(d1)
d2[5] = 'ok'

del d2[5]
d2.items()

for k,v in d2.items():
    print('key: ',k,'val: ',v)

#%%