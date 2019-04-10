#!/usr/bin/env python
# -*- coding: utf-8 -*-

#На всякий случай прописываю новую функцию mini, которая аналогична min
import numpy as np
def mini(data):
    mins=data[0]
    for i in range(1,len(data)):
        if mins>data[i]:
            mins=data[i]
    return mins

def selection_sort(a):
    a1=a.tolist()
    i=0
    while i < (len(a1) - 1):
        q=a1.index(mini(a1[i:]),i)
        a1[i], a1[q] = a1[q], a1[i]
        i+=1
    a=np.array(a1)
    return a
