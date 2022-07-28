# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 14:03:23 2020

@author: qin790
"""
import numpy as np


def Slides(nodes, slides):
    #base case
    n = len(nodes)
    if n ==1:
        return
    elif n ==2:
        slides[nodes[0],nodes[1]]=1
        return slides
    
    #divide two two halves
    m = int(n/2)
    first=nodes[:m]
    second=nodes[m:n]
    
    #print ("first second", first, second)
    #in second connect the first to all other nodes
    for j in second:
        if j != nodes[m]:
            #print("second", nodes[m], j)
            slides[nodes[m],j]=1
    #connect all the nodes in the first to m
    for i in first:
        if i != m:
            #print ("first", i, m)
            slides[i,nodes[m]]=1

    
    Slides(first, slides) 
    Slides(second, slides)
    return slides

def Check(slides, n):
    for i in range(n):
        for j in range (n):
            if i >= j:
                pass
            
            elif slides[i, j]==1 and j > i:
                return True
            else:
                for m in range(n):
                    if m > i and m < j:    
                        if slides[i, m]+slides[m, j]== 2:
                            return True
                else:
                    print("i, j", i, j)
                    return False

def main(n):
    nodes=[i for i in range(n)]
    slides = np.zeros((n,n))
    return Slides(nodes, slides)

if __name__ == '__main__':
    n = 10
    slides = main(n)
    print (slides)
    print ("total slides", np.sum(slides))

    if Check(slides, n):
        print("successful")
    else:
        print("not successfull")