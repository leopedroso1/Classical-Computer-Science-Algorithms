# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 18:03:54 2020

@author: Leonardo
"""


    
def findKLargest(number_list, k):
        
    idx_left = 0
    idx_right = len(number_list) - 1
    
    while idx_left <= idx_right:
            
        pivotIndex = partition(number_list, idx_left, idx_right)
            
        if pivotIndex == len(number_list) - k:
                
            return number_list[pivotIndex]
            
        elif pivotIndex > len(number_list) - k:
                
            idx_right = pivotIndex - 1
                
        else:
                
            idx_left = pivotIndex + 1

    return -1

    
def partition(number_list, low, high): # Creates the partition
        
    pivot = number_list[high]
        
    index = low
        
    for j in range(low, high):
            
        if number_list[j] <= pivot:
                
            number_list[index], number_list[j] = number_list[j], number_list[index]
                
            index += 1
                
    number_list[index], number_list[high] = number_list[high], number_list[index]
        
    return index
        
        


print(findKLargest([5, 7, 2, 3, 4, 1, 6], 3))
# Expected Solution: 5