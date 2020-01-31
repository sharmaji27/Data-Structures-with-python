# -*- coding: utf-8 -*-
"""
MERGE SORT

"""

def merge_sort(a):
    if len(a)==1:
        return
    
    middle = len(a)//2
        
    left_half = a[:middle]
    right_half = a[middle:]
    
    merge_sort(left_half)
    merge_sort(right_half)
    
    i = 0
    j = 0
    k = 0
    
    while i<len(left_half) and j<len(right_half):
        if left_half[i] < right_half[j]:
            a[k] = left_half[i]
            i+=1
        else:
            a[k] = right_half[j]
            j+=1
        k+=1
    
    while i < len(left_half):
        a[k]=left_half[i]
        i+=1
        k+=1
    
    while j < len(right_half):
        a[k]=right_half[j]
        j+=1
        k+=1
        
a=[4,1,6,-7,8,3,0]
merge_sort(a)
print(a)
    