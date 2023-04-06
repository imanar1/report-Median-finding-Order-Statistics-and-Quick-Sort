# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 22:29:22 2023

@author: Shaha
"""



import random

def partitionran(a, p, r, x):
    for i in range(p, r+1): 
        if a[i] == x: 
            a[i], a[r] = a[r], a[i]
            break
    
    i = p - 1
    for j in range(p, r):
        if a[j] <= a[r]:
            i += 1 
            a[i], a[j] = a[j], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return i+1 
 
def selectkthSmallestrand(arr, l, r, k):
   
    # if k is smaller than number of elements in array
    if (k > 0 and k <= r - l + 1):
        # Randomly select a pivot element
        pivot_index = random.randint(l, r)
        arr[pivot_index], arr[r] = arr[r], arr[pivot_index]
        
        # Partition the array around the pivot element and get its position in the sorted array
        index = partitionran(arr, l, r, arr[r])
        # if position is same as k
        if (index - l == k - 1):
            return arr[index]
        
        # If position is more, recur for left subarray
        if (index - l > k - 1):
            return selectkthSmallestrand(arr, l, index - 1, k)
        # Else recur for right subarray
        return selectkthSmallestrand(arr, index + 1, r, k - index + l - 1)
    print("Index out of bound")
    



    
# find median (n/2)    
def medianOfMedians(arr, l, r, chunkSize):
    n = r - l + 1
    if n <= chunkSize:
        arr = sorted(arr[l:r+1])
        return arr[n//2]
    medians = []
    for i in range(l, r+1, chunkSize):
        subArr = arr[i:min(i+chunkSize, r+1)]
        subArr = sorted(subArr)
        median = subArr[len(subArr)//2]
        medians.append(median)
    pivot = medianOfMedians(medians, 0, len(medians) - 1, chunkSize)
    pivotIndex = arr.index(pivot, l, r+1)
    pivotIndex = partitionran(arr, l, r, pivotIndex)
    k = pivotIndex - l + 1
    if k == n//2:
        return arr[pivotIndex]
    elif n//2 < k:
        return medianOfMedians(arr, l, pivotIndex - 1, chunkSize)
    else:
        return medianOfMedians(arr, pivotIndex + 1, r, chunkSize)
def findMedian2(a, p, r):
    L = []
    for i in range(p, r+1):
        L.append(a[i])
    L.sort()
    return L[(r-p+1)//2] 



def KthSmallestRandomized(a, p, r, k):
    '''
    the pivot random 
    '''
    n = r - p + 1
    median = []
    i = 0
    while i < n//5:
        median.append(findMedian2(a, p+5*i, p+5*i+4))
        i += 1
    if i*5 < n:
        median.append(findMedian2(a, p+5*i, p+5*i+(n%5-1)))
        i += 1
    if i == 1:
        medOfmed = median[i-1]
    else:
        pivot = random.randint(0, i-1)
        medOfmed = median[pivot]
          
    q = partitionran(a, p, r, medOfmed)
    i = q - p + 1 
    if i == k:
        return a[q]
    elif i > k:
        return KthSmallestRandomized(a, p, q-1, k)
    else:
        return KthSmallestRandomized(a, q+1, r, k-i)

    
    

def findMedian(arr, chunkSize):
    """
    This function returns the median of the given array (`arr`), using the `medianOfMedians` function.
    The `chunkSize` parameter is used to determine the size of the chunks to use in the `medianOfMedians` function.
    """
    return medianOfMedians(arr, 0, len(arr) - 1, chunkSize)


def quickSort(arr, low, high):
    """
    This function performs the quick sort algorithm on a portion of the given array (`arr`) 
    between the indices `low` and `high` (inclusive).
    
    The function partitions the array around a pivot, and then recursively sorts the sub-arrays
    to the left and right of the pivot until the entire portion of the array is sorted.
    """
    if low < high:
        # Partition the array and get the index of the pivot
        p=selectkthSmallestrand(arr,low ,high,int((high-low)/2 +1) )
        pi = partitionran(arr, low, high, high)
        # Recursively sort the left portion of the array (before the pivot)
        quickSort(arr, low, pi - 1)
        # Recursively sort the right portion of the array (after the pivot)
        quickSort(arr, pi + 1, high)


def median_of_medians5rand(scores, rank):
# If the number of scores is less than or equal to 5, sort the scores and return the score at the rank-th position
    if len(scores) <= 5:
        scores.sort()
        return scores[rank-1]
  # Split the scores into sublists of size 5

    sublists = [scores[i:i+5] for i in range(0, len(scores),5)]
  # Find the median of each sublist
 
    medians = [median_of_medians5rand(sublist, int(len(sublist)/2)) for sublist in sublists]
        # Randomly select a pivot element from the medians

    pivot = random.choice(medians)

    lower = [x for x in scores if x < pivot]
    upper = [x for x in scores if x > pivot]

    if rank <= len(lower):
        return median_of_medians5rand(lower, rank)
    elif rank >= len(scores) - len(upper):
        return median_of_medians5rand(upper, rank - (len(scores) - len(upper)))
    else:
        return pivot
    
    
def median_of_medians3rand(scores, rank):
# If the number of scores is less than or equal to 5, sort the scores and return the score at the rank-th position
    if len(scores) <= 3:
        scores.sort()
        return scores[rank-1]
  # Split the scores into sublists of size 5

    sublists = [scores[i:i+3] for i in range(0, len(scores),3)]
  # Find the median of each sublist
 
    medians = [median_of_medians5rand(sublist, int(len(sublist)/2)) for sublist in sublists]
        # Randomly select a pivot element from the medians

    pivot = random.choice(medians)

    lower = [x for x in scores if x < pivot]
    upper = [x for x in scores if x > pivot]

    if rank <= len(lower):
        return median_of_medians5rand(lower, rank)
    elif rank >= len(scores) - len(upper):
        return median_of_medians5rand(upper, rank - (len(scores) - len(upper)))
    else:
        return pivot    
    
def median_of_medians7rand(scores, rank):
# If the number of scores is less than or equal to 5, sort the scores and return the score at the rank-th position
    if len(scores) <= 7:
        scores.sort()
        return scores[rank-1]
  # Split the scores into sublists of size 5

    sublists = [scores[i:i+7] for i in range(0, len(scores),7)]
  # Find the median of each sublist
 
    medians = [median_of_medians5rand(sublist, int(len(sublist)/2)) for sublist in sublists]
        # Randomly select a pivot element from the medians

    pivot = random.choice(medians)

    lower = [x for x in scores if x < pivot]
    upper = [x for x in scores if x > pivot]

    if rank <= len(lower):
        return median_of_medians5rand(lower, rank)
    elif rank >= len(scores) - len(upper):
        return median_of_medians5rand(upper, rank - (len(scores) - len(upper)))
    else:
        return pivot

#a=[10023,100845,12290,12345,3345,22134,1124567,4545,1234,7789,3345,123]


#print(a)
#size=len(a)
#print('Median-finding algorithms')

#rank=int(input('Enter the rank :'))
#print("The",rank,"kth smallest element :", selectkthSmallestrand(a, 0, size-1, rank))

#print('the',rank,'kth smallest element (random):',KthSmallestRandomized(a, 0, size-1, rank))


#print('----Median of Median Algorithms----')


#print(" median of median algorithms with group 3: ", median_of_medians5rand(a,rank))



#print('---Median of the array----')
#m=medianOfMedians(a, 0, size-1, rank)
#print(m)



#q=quickSort(a, 0, size- 1)

#print("----Sorted array ----", a)