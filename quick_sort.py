#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
#Я не смогла придумать ничего изобретательнее, чем решение Стаса
#Так что я просто его немного улучшила
#На уроке реализовала сортировку с созданием новых списков, что не пошло в зачет
#Не вижу смысла переименовывать переменные, очевидно, кем я вдохновлялась
#Могу сказать, что это сортировка Хоара
#А еще, чтобы создать имитацию деятельности, я сравнила модификацию с оригинальным решением Стаса
#И модификация лучше (но ненамного)
def quick_sort(massive, left=0, right=None):
    if right == None:
        right = len(massive) - 1
    if left >= right:
        return massive
    left_m = left
    right_m = right
    pivot = random.choice(massive[left:right])
    while left <= right:
        while massive[left] < pivot:
            left += 1
        while massive[right] > pivot:
            right -= 1
        if left <= right:
            massive[left], massive[right] = massive[right], massive[left]
            left += 1
            right -= 1
    quick_sort(massive, left_m, right)
    quick_sort(massive, left, right_m)
    return massive 