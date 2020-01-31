# -*- coding: utf-8 -*-
"""
SELECTION SORT

"""

def selection_sort(a):
    for i in range(len(a)-1):
        min_index = i
        for j in range(i+1,len(a)):
            if a[j]<a[min_index]:
                min_index = j
        if min_index!=i:
            a[i],a[min_index] = a[min_index],a[i]
    return a

a = [4,1,-9,6,-7,5]

print(selection_sort(a))