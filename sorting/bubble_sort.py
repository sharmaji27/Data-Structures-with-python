# -*- coding: utf-8 -*-
"""
BUBBLE SORT

"""

def bubble_sort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
    return a

a = [4,1,9,6,7,5]

print(bubble_sort(a))