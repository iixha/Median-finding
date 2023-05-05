# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 00:14:38 2023

@author: ACER
"""

import time
#import numpy as np
import QuickSortLinkedList
import QuickSortArray
import QuickSortTree
import SelectionSortHeap
import SelectionSort_LinkedList
import SelectionSortArray




def findMedian(root):
    if (root == None):
        return 0
        count = counNodes(root)
        currCount = 0
        current = root

    while (current != None):

        if (current.left == None):

            # count current node
            currCount += 1

            # check if current node is the median
            # Odd case
            if (count % 2 != 0 and
                    currCount == (count + 1) // 2):
                return prev.data

            # Even case
            elif (count % 2 == 0 and
                  currCount == (count // 2) + 1):
                return (prev.data + current.data) // 2

            # Update prev for even no. of nodes
            prev = current

            # Move to the right
            current = current.right

        else:

            """ Find the inorder predecessor of current """
            pre = current.left
            while (pre.right != None and
                    pre.right != current):
                pre = pre.right

            """ Make current as right child
                of its inorder predecessor """
            if (pre.right == None):

                pre.right = current
                current = current.left
            else:

                pre.right = None

                prev = pre

                # Count current node
                currCount += 1

                # Check if the current node is the median
                if (count % 2 != 0 and
                        currCount == (count + 1) // 2):
                    return current.data

                elif (count % 2 == 0 and
                      currCount == (count // 2) + 1):
                    return (prev.data + current.data) // 2

                # update prev node for the case of even
                # no. of nodes
                prev = current
                current = current.right
                
def findMedianlinked(self): 

        #if the linked list is empty, return None  
        if self.head is None: 
            return None
        #create two pointers, slow and fast  
        slow = fast = self.head
        #loop until fast reaches end of the linked list  
        while (fast is not None and fast.next is not None): 
            #move slow pointer one node at a time  
            slow = slow.next
            #move fast pointer two nodes at a time  
            fast = fast.next.next
        #return the data at the middle node of the linked list                                                                                                                                              return slow.data
        return slow.data
    
def findMedianArray(a, n):
    if n % 2 != 0:
        return float(a[int(n / 2)])
    return float((a[int((n - 1) / 2)] + a[int(n / 2)]) / 2.0)





def Menu():
    print("------------------------")
    print("1-Quick sort using linked list\n2-Quick sort using array \n3-Quick sort using Binary searsh")
    print("4-Selection sort using heap \n5-Selection sort using linked list \n6-Selection sort using Array")
    print("------------------------")
    
    
    choice = int(input('Enter your choice: '))
  

# while the choice not = to 0 it will ask to enter another number r
    while choice != 0 :
       if choice == 1:     
         print("1------------------------")
         print(findMedianlinked(QuickSortLinkedList.root.QuickSort(QuickSortLinkedList.root.head))) 
         print('TIME : ' ,time.process_time()) 
         Menu()
         option = int(input('Enter your choice: '))
        
       elif choice == 2:
         print("2 ------------------------")
         print(findMedianArray(QuickSortArray.quickSort(QuickSortArray.arr, 0,QuickSortArray.d )), QuickSortArray.n )
         print('TIME : ' ,time.process_time()) 
         Menu()
         option = int(input('Enter your choice: '))
           
       elif choice == 3:
         print("3 ------------------------")
         print(findMedian(QuickSortTree.quickSort(QuickSortTree.root))) 
         print('TIME : ' ,time.process_time()) 
         Menu()
         option = int(input('Enter your choice: '))
            
       elif choice == 4: 
           print("4 ------------------------")
           print(findMedian(SelectionSortHeap.heapSort(SelectionSortHeap.arr))) 
           print('TIME : ' ,time.process_time()) 
           Menu()
           option = int(input('Enter your choice: '))
         
       elif choice == 5:
           print("5 ------------------------")
           print(findMedianArray(SelectionSortArray.selectionSort(SelectionSortArray.arr , SelectionSortArray.size))) 
           print('TIME : ' ,time.process_time()) 
           Menu()
           option = int(input('Enter your choice: '))
           
       elif choice == 6:
          print("5 ------------------------")
          print(findMedianlinked(SelectionSort_LinkedList.selectionSort(SelectionSort_LinkedList.head))) 
          print('TIME : ' ,time.process_time()) 
          Menu()
          option = int(input('Enter your choice: '))   
          
       elif choice == 7: 
         print ('Invalid option. please enter a number between 0 and 4')
         Menu()
         option = int(input('Enter your choice: '))
                
                  
                  
                
                    
Menu()
