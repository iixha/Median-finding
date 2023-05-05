# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 01:36:42 2023

@author: Maram
"""

import time

# Python3 implementation of the approach  

  
# Linked List Node  

class Node: 

      

    def __init__(self, val): 

        self.data = val 

        self.next = None

  
# Function to sort a linked list  
# using selection sort algorithm 
# by swapping the next pointers  

def selectionSort(head):  

  

    a = b = head  

  

    # While b is not the last node  

    while b.next:  

  

        c = d = b.next
        # While d is pointing to a valid node  
        while d:  

  

            if b.data > d.data:  

  

                # If d appears immediately after b  

                if b.next == d:  

  

                    # Case 1: b is the head  

                    # of the linked list  

                    if b == head:  

  

                        # Move d before b  

                        b.next = d.next

                        d.next = b  

  

                        # Swap b and d pointers  

                        b, d = d, b  

                        c = d  

  

                        # Update the head  

                        head = b  

  

                        # Skip to the next element  

                        # as it is already in order  

                        d = d.next

                      

                    # Case 2: b is not the head  

                    # of the linked list  

                    else:  

  

                        # Move d before b  

                        b.next = d.next

                        d.next = b  

                        a.next = d  

  

                        # Swap b and d pointers  

                        b, d = d, b  

                        c = d  

  

                        # Skip to the next element  

                        # as it is already in order  

                        d = d.next

                      

                # If b and d have some non-zero  

                # number of nodes in between them  

                else: 

  

                    # Case 3: b is the head  

                    # of the linked list  

                    if b == head:  

  

                        # Swap b.next and d.next  

                        r = b.next

                        b.next = d.next

                        d.next = r  

                        c.next = b  

  

                        # Swap b and d pointers  

                        b, d = d, b  

                        c = d  

  

                        # Skip to the next element  

                        # as it is already in order  

                        d = d.next

  

                        # Update the head  

                        head = b  

                      

                    # Case 4: b is not the head 

                    # of the linked list  

                    else:  

  

                        # Swap b.next and d.next  

                        r = b.next

                        b.next = d.next

                        d.next = r  

                        c.next = b  

                        a.next = d  

  

                        # Swap b and d pointers  

                        b, d = d, b  

                        c = d  

  

                        # Skip to the next element  

                        # as it is already in order  

                        d = d.next

                      

            else: 
                # Update c and skip to the next element  

                # as it is already in order  

                c = d  

                d = d.next

  

        a = b  

        b = b.next

      

    return head  

# Function to print the list  

def printList(head):  

  

    while head:  

        print(head.data, end = " ")  

        head = head.next

  
# Driver Code  

if __name__ == "__main__": 

    head = Node(52)  
    head.next = Node(48)  
    head.next.next = Node(35)  
    head.next.next.next = Node(22)
    head.next.next.next.next = Node(20)
    

    # printList(head)  
    # print('TIME : ' ,time.process_time())
           
       
          
          
          
