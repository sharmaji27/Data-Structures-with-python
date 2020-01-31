# -*- coding: utf-8 -*-
"""
INSERTION SORT

"""

def insertion_sort(a):
    for i in range(1,len(a)):
        j= i-1
        while(a[j]>a[j+1] and j>=0):
            a[j],a[j+1] = a[j+1],a[j]
            j=j-1
    return a

a = [4,1,9,-6,7,5]

print(insertion_sort(a))
