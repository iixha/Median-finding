# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 00:58:13 2023

@author: ACER
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 01:17:48 2023

@author: HANA
"""


import numpy as np
import time

# Helper function that allocates a new node with the given data and None left and right pointers.
class newNode:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def InsertTreeb(root, data): 
    if root is None: 
       return newNode(data) 
  
    else: 
        if data <= root.data: 
            cur = InsertTreeb(root.left, data) 
            root.left = cur 
        else: 
            cur = InsertTreeb(root.right, data) 
            root.right = cur 

    return root


""" Function to count nodes in
    a binary search tree using
     Morris Inorder traversal"""


def counNodes(root):
    # Initialise count of nodes as 0
    count = 0

    if (root == None):
        return count

    current = root
    while (current != None):

        if (current.left == None):

            # Count node if its left is None
            count += 1

            # Move to its right
            current = current.right

        else:
            """ Find the inorder predecessor of current """
            pre = current.left

            while (pre.right != None and
                   pre.right != current):
                pre = pre.right

            """ Make current as right child of its
            inorder predecessor """
            if (pre.right == None):

                pre.right = current
                current = current.left
            else:

                pre.right = None

                # Increment count if the current
                # node is to be visited
                count += 1
                current = current.right

    return count

def quickSort(head): 
    if head is None or head.right is None: 
        return head 

    pivot = partition(head) 

    pivot.left = quickSort(pivot.left) 

    pivot.right = quickSort(pivot.right) 

    return pivot 

  
def partition(head): 

    pivot = head 

    prev = None

    curr = head 

    while curr is not None: 

        if curr.data < pivot.data:  

           prev = insertBeforePivot(prev, curr, pivot)  

        curr = curr.right  

    return pivot  

def insertBeforePivot(prev, curr, pivot):  

    if prev is None:  

        curr.right = pivot 

        return curr  

    else:  

        prev.right = curr.right  
        
        curr.right = pivot 
        
def printList(head): 
    temp = head 
    while temp is not None: 
        print (temp.data, end=" ")       
        temp=temp . right
       
root = newNode(0)
arr=np.loadtxt("covid.CSV", delimiter=",")
for x in arr:
    InsertTreeb(root, x)  
n = counNodes(root)
# quickSort(root) 
# printList(root)
# print('TIME : ' ,time.process_time()) 
