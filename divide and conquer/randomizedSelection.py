# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 08:38:50 2020

@author: Vishnu
"""


def swapValues(arr, i, j):
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t


def chooseRandomPivot(array, startIndex, endIndex):
    return endIndex


def arrayPartition(array, startIndex, endIndex):
    randomPivot = chooseRandomPivot(array, startIndex, endIndex)
    swapValues(array, randomPivot, endIndex)
    pivot = startIndex
    for i in range(startIndex, endIndex):
        if array[i] < array[endIndex]:
            swapValues(array, i, pivot)
            pivot += 1
    swapValues(array, pivot, endIndex)
    return pivot


def randomizedSelection(array, startIndex, endIndex):
    global ithOrderIndex
    pivot = arrayPartition(array, startIndex, endIndex)
    if pivot == ithOrderIndex:
        return array[pivot]
    elif pivot > ithOrderIndex:
        return randomizedSelection(array, startIndex, pivot - 1)
    else:
        return randomizedSelection(array, pivot + 1, endIndex)


array = [8, 4, 33, 2, 55, 1, 77, 21, 65, 10]


ithOrderIndex = 2

for i in range(10):
    ithOrderIndex = i
    print(randomizedSelection(array, 0, len(array)-1))
