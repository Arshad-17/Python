# -*- coding: utf-8 -*-
"""
@author: arshad
"""

# Quick sort

def quick_sort(lst):
    
    length = len(lst)
    if length <= 1:
        return lst
    else:
        pivot = lst.pop()
        
    items_greater = []
    items_lower = []
    
    for i in lst:
        if i> pivot:
            items_greater.append(i)
            
        else:
            items_lower.append(i)
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

print(quick_sort([9,4,4,1,3,6]))




