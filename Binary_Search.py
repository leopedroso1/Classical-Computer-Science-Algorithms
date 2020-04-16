# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 16:54:39 2020

@author: Leonardo
"""

############################## Binary Search!!  ##############################

# Introduction: Given a sorted array of "N" elements, write a function to search an element X in the array.
# Brute force approach is the Linear Search! You'd run all the array looking for the element X >>>> O(n)


# How it works: Given a SORTED array, you will search repeatedly dividing the seach interval in half
#               For this, pick the middle of the array as a pivot. If the value of the search key is less than the item in the middle of the interval, 
#               narrow the interval to the lower half. Otherwise narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.

# Complexity: O(log n)


def binarySearch_Recursive(myList, left_pointer, right_pointer, x):
    
    # Check the base case
    if right_pointer >= left_pointer:
        
        # calculate the middle of the array
        middle = left_pointer + (right_pointer - left_pointer) // 2
        
        # if the element is right in the middle return the middle index
        if myList[middle] == x:
            
            return middle

        # if the element is smaller than mid. Then can be presented in the left subarray
        elif myList[middle] > x:
            
            return binarySearch_Recursive(myList, left_pointer, middle - 1, x)        
        
        # if the element is bigger than mid. Then can be presented in the right subarray
        else:
       
            return binarySearch_Recursive(myList, middle + 1, right_pointer, x)
    
    else:

        # if not found...finish!
        return -1 


def binarySearch_Iterative(myList, left_pointer, right_pointer, x):
    
    while left_pointer <= right_pointer:

        # calculate the middle of the array
        middle = left_pointer + (right_pointer - left_pointer) // 2
        
        if myList[middle] == x:
            
            return middle
        
        # If x is greater -> ignore the left half
        elif myList[middle] < x:
            
            left_pointer = middle + 1

        # if x is smaller -> ignore the right half
        else:
            
            right_pointer = middle - 1
        
    return - 1





array = [2, 1, 11, 70, 23, 5, 3, 4, 10, 20] # <<< change here as you wish 
x = 23 # <<< Change the element to be searched as you wish

array.sort() # Secures a sorted array
myList = array.copy() # Copy it..

result_1 = binarySearch_Recursive(myList, 0, len(myList) - 1, x)
result_2 = binarySearch_Iterative(myList, 0, len(myList) - 1, x)

if result_1 != -1 or result_2 != -1:

    print("Recusive Search - Element found at index %d" % result_1)
    print("Iterative Search - Element found at index %d" % result_2)
    
else:
    
    print("Element not present in array")