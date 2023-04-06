# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 22:30:50 2023

@author: Shaha
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BST:
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)
            
    def _insert(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(data, node.right)
    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data, end=' ')
        self.inorder(root.right)
    
                 
  
    def kthSmallest(self, node, k, cnt):
    # Check if the node is None
     if node is None:
        # If it is, return immediately
        return
    
    # Recursively call the function on the left child of the node
     self.kthSmallest(node.left, k, cnt)
     
    # Increment the counter
     cnt[0] += 1
    
    # Check if the counter is equal to the target value k
     if cnt[0] == k:
        # If it is, print the data of the node and return
        print("The kth smallest element is:", node.data)
        return
    
    # Recursively call the function on the right child of the node
     self.kthSmallest(node.right, k, cnt)
     def medianOfMedians(self, values, l, r, chunkSize):
    # Calculate the size of the subarray
       n = r - l + 1

    # Base case: if the size of the subarray is less than or equal to chunkSize, sort the subarray and return the median
       if n <= chunkSize:
        values = sorted(values[l:r+1])
        return values[n//2]

    # Create a list to store the medians of the subarrays
       medians = []

    # Loop through the subarrays
       for i in range(l, r+1, chunkSize):
        # Get the current subarray
        subArr = values[i:min(i+chunkSize, r+1)]

        # Sort the current subarray
        subArr = sorted(subArr)

        # Find the median of the current subarray
        median = subArr[len(subArr)//2]

        # Add the median to the list of medians
        medians.append(median)

    # Use the medians to find a pivot
       pivot = self.medianOfMedians(medians, 0, len(medians) - 1, chunkSize)

    # Find the index of the pivot in the original array
       pivotIndex = values.index(pivot, l, r+1)

    # Partition the original array around the pivot
       pivotIndex = self.partition(values, l, r, pivotIndex)

    # Calculate k, the number of elements in the left subarray
       k = pivotIndex - l + 1

    # If k is equal to n//2, the pivot is the median
       if k == n//2:
        return values[pivotIndex]
    # If n//2 is less than k, the median is in the left subarray
       elif n//2 < k:
        return self.medianOfMedians(values, l, pivotIndex - 1, chunkSize)
    # If n//2 is greater than k, the median is in the right subarray
       else:
        return self.medianOfMedians(values, pivotIndex + 1, r, chunkSize)

 
      

#bst = BST()
#arr=[25,24,33,39,3,18,19,31,23,49,45,16,1,26,40,22,15,20,24,4,13,34]
#a=[10023,100845,12290,12345,3345,22134,1124567,4545,1234,7789,3345,123]
#for ele in a:
        #bst.insert(ele)
#cnt = [0]
    #print('BST')

#rank=int(input('Enter the rank :'))
#bst.kthSmallest(bst.root, rank, cnt)
#bst.inorder(bst.root)
