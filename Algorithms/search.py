# -*- coding: utf-8 -*-
"""
@author: arshad ali
"""

lst = [5, 8, 4, 6, 9, 2]

lst2 = [2, 6, 7, 18, 23, 46]

# Linear Search

def search(lst: list, n: int) -> bool:
    """This method implements linear search method"""
    i = 0
    while i< len(lst):
        if lst[i] == n:
            return True
        i = i+1
    return False

print(search(lst, 28))
print(search(lst, 2))


# Binary Search


def binary_search(lst: list, n: int) -> bool:
    """This algorithm expects the array to be sorted"""
    start_index = 0
    end_index = len(lst) - 1
    
    while start_index <= end_index:
        mid_index = start_index + (end_index - start_index)//2
        mid_value = lst[mid_index]
        if mid_value == n:
            return mid_index
        elif n < mid_value:
            end_index = mid_index - 1
        else:
            start_index = mid_index + 1
            
    return "Not Found"

print(binary_search(lst2, 24))
print(binary_search(lst2, 2))
    
    
