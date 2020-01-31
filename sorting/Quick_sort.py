# -*- coding: utf-8 -*-
"""
QUICK SORT

"""
def quick_sort(a,l,h):
    if l>=h:
        return
    pivot = partition(a,l,h)
    quick_sort(a,l,pivot-1)
    quick_sort(a,pivot+1,h)


def partition(a,l,h):        
    p = (l+h)//2
    a[p],a[h] = a[h],a[p]
    i = l
    
    for j in range(l,h):
        if a[j]<=a[h]:
            a[j],a[i] = a[i],a[j]
            i+=1
    a[i],a[h] = a[h],a[i]
    
    return i
    
a = [4,1,9,6,7,5]
#a=[-2,-1,0,1,0,-1,-2]

quick_sort(a,0,len(a)-1)

print(a)