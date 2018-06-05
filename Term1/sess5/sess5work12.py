# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 17:52:47 2018

@author: maser
"""

import numpy as np
import matplotlib.pyplot as plt

#1
def reverse_array(input_array):
    rev = input_array[::-1]
    return rev
#2
def sort_array(input_array):
    sorted_array=np.sort(input_array)
    return sorted_array

#3
def plot_matrix(seq_0, seq_1):
    mat=np.zeros(shape=(len(seq_0),len(seq_1)))
    for x in range(0,len(seq_0)):
        for y in range(0,len(seq_1)):
            if seq_0[x]==seq_1[y]:
                mat[x,y]=1    
    plt.matshow(mat)
    plt.show()

#4
def histogram(labA,labB):
    labA=open(labA)
    labB=open(labB)
    valueslabA=[]
    valueslabB=[]
    dictA={}
    dictB={}
    for line in labA:
        if not line.strip():
            continue
        else:
            keys,values=line.split()
            valueslabA.append(float(values))
            dictA.update({keys:float(values)})
    for line in labB:
        if not line.strip():
            continue
        else:
            keys,values=line.split(",")
            valueslabB.append(float(values))
            dictB.update({keys:float(values)})
    listA=[]
    listB=[]
    for key in dictA:
        if key in dictB:
            listA.append(dictA[key])
    for key in dictB:
        if key in dictA:
            listB.append(dictB[key])        
    labA.close()
    labB.close() 
    
    plt.subplot(121)
    plt.hist(valueslabA,alpha=0.5,facecolor="green")
    plt.hist(valueslabB,alpha=0.5,facecolor="red")
    plt.xlabel("Gene Expression Level")
    plt.ylabel("Expression Frequency")
    plt.title("Histogram")
    plt.subplot(122)
    plt.scatter(listA,listB,facecolor="red")
    plt.xlabel("Expression Level Lab A")
    plt.ylabel("Expression Level Lab B")
    plt.title("Scatter plot")
    plt.show()

if __name__ == '__main__':
    print(reverse_array(([1,2,3])))
    print(sort_array(([4,2,5,7,3,1,2,3,6])))
    print(plot_matrix("HELLOMUM","HELLOMUM"))
    print(histogram("resultslabA.txt","resultslabB.txt"))
  
  
