# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 02:13:25 2023

@author: ACER
"""
import numpy as np 
import time
def selectionSort(array, size):


    for ind in range(size):

        min_index = ind
 

        for j in range(ind + 1, size):

            # select the minimum element in every iteration

            if array[j] < array[min_index]:

                min_index = j

         # swapping the elements to sort the array

        (array[ind], array[min_index]) = (array[min_index], array[ind])
 

arr = np.loadtxt("covid.CSV", delimiter=",")

size = len(arr)

selectionSort(arr, size)

print('The array after sorting in Ascending Order by selection sort is:')

print(selectionSort(arr, size))
print(time.process_time())