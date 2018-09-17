# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 12:31:00 2018

@author: briha
"""
#value 
x= 0 
#header for table
print('decimal\t\tbinary\t\thex')
#table and columns
for x in range(8):
    print(x, '\t', bin(x),'\t','\t', hex(x))
for x in range(8,32):
    print(x, '\t', bin(x),'\t', hex(x))
    
