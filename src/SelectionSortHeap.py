# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 20:50:41 2023

@author: extra
"""
import numpy as np
import time
import heapq 
from heapq import heappush, heappop, heapify
import math
 
# Function to find the median of stream of data
# Python code to find the median of a given array 
# using heapify data structure

       

      

def heapifyy(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2
  
 # See if left child of root exists and is
 # greater than root
  
    if l < n and arr[i] < arr[l]:
        largest = l
  
 # See if right child of root exists and is
 # greater than root
  
    if r < n and arr[largest] < arr[r]:
        largest = r
  
 # Change root, if needed
  
    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])  # swap
  
  # Heapify the root.
  
        heapifyy(arr, n, largest)
  
  
# The main function to sort an array of given size
  
def heapSort(arr):
    n = len(arr)
  
 # Build a maxheap.
 # Since last parent will be at ((n//2)-1) we can start at that location.
  
    for i in range(n // 2 - 1, -1, -1):
        heapifyy(arr, n, i)
  
 # One by one extract elements
  
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])  # swap
        heapifyy(arr, i, 0)
  
  
# Driver code to test above


arr=np.loadtxt("covid.CSV", delimiter=",")

# heapSort(arr)
# n = len(arr)

# print('median of Sorted array is by using selection sort ')
# print(streamMed(myArray1,n))
# print(time.process_time())