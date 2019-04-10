#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
#Модифицированная функция бинарного поиска, возвращает индекс, на который нужно поставить value
def binary_insert(data, value):
    l=0
    h=len(data)-1
    while l<=h:
        m=(h+l)//2
        v=data[m]
        if v==value:
            return m+1 #Т.к.мы все равно с правого конца сортируем, сокращаем число итераций
        elif v<value:
            l=m+1
        elif v> value:
            h=m-1
    return l #Подходит и тогда, когда value меньше всех элементов, и когда больше
#Функция принимает массив и возвращает массив, внутри функция перестановок
def insertion_sort(a):
    a1=a.tolist()
    r=1
    while r < len(a1):
        z=binary_insert(a1[0:r], a1[r])
        for i in range(len(a1[0:r]),-1,-1):
            if z<=(i-1):
                a1[i-1],a1[i]=a1[i],a1[i-1]
            else:
                break
        r+=1
    a=np.array(a1)
    return a
