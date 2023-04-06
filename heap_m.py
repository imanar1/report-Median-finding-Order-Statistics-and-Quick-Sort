# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 22:30:08 2023

@author: Shaha
"""

import heapq


def partition(arr):
    
    '''
    In this implementation, we first extract the pivot element, 
    and then use a min heap to store elements that are less than or 
    equal to the pivot. Elements that are greater than the pivot 
    are stored in the heap with the pivot as the value, and the pivot 
    is updated to the new value. This results in a heap where 
    all elements less than or equal to the pivot are stored 
    in the left half of the heap, while all elements 
    greater than the pivot are stored in the right half of the heap.
    The final result is a list representation of the heap.
    '''
    low, high = 0, len(arr) - 1
    pivotIndex = high
    pivot = arr[pivotIndex]
    heap = []
    for element in arr:
        if element <= pivot:
            heapq.heappush(heap, element)
        else:
            heapq.heappush(heap, pivot)
            pivot = element
    return list(heap)

def kthSmallest(arr, k):
    heap = []
    # Push the elements of the array into the heap
    for element in arr:
        heapq.heappush(heap, element)
    # Pop the smallest element k times to get the kth smallest element
    for i in range(k - 1):
        heapq.heappop(heap)
    return heapq.heappop(heap)
    
    
    
def findMedian(arr, chunkSize):
    return median_of_medians5(arr,chunkSize)

def median_of_medians5(arr, rank):

    # If the number of scores is less than or equal to 5, sort the scores and return the score at the rank-th position
    if len(arr) <= 5:
        arr.sort()
        return arr[rank-1]

    # Split the scores into sublists of size 5
    sublists = [arr[i:i+5] for i in range(0, len(arr),5)]
    medians = [sorted(sublist)[len(sublist)//2] for sublist in sublists]

    pivot = heapq.nsmallest(len(medians)//2+1, medians)[-1]

    lower = [x for x in arr if x < pivot]
    upper = [x for x in arr if x > pivot]

    if rank <= len(lower):
     return median_of_medians5(lower, rank)
    elif rank > len(arr) - len(upper):
     return median_of_medians5(upper, rank - (len(arr) - len(upper)))
    else:
     return pivot
 


#arr=[10023,100845,12290,12345,3345,22134,1124567,4545,1234,7789,3345,123]
#size=len(arr)
#print('heap:')
#rank=int(input('Enter the rank:'))
#print("The kth smallest element is:", kthSmallest(arr,rank))
#print("Algorthms to median_of_medians5 is:", findMedian(arr,rank))