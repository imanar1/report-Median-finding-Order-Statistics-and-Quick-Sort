def partition2(a, p, r, x):
    '''
    Parameters
    ----------
    a : array 
    p : start index
    r :  end index
    x :  pivot value
--
 Next, it performs a standard partitioning operation
 to sort the elements in the subarray a[p..r] 
 into two groups: elements less than or equal to the pivot
 and elements greater than the pivot.
 This is done by maintaining two pointers i and j. 
 The pointer i starts from p - 1 and moves right whenever an element a[j] 
 less than or equal to the pivot is encountered. 
 The element a[j] is then swapped with the element at the index i+1.
 The partitioning continues until j reaches r.
    '''
    # we should find out medOfmed's index i value in the a[p..r]
    # swap a[i], a[r] in order to make a[r] as a pivot 
    
    
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
 
def selectkthSmallest(arr, l, r, k):
    '''
  
    Parameters
    ----------
    a : array 
    p : start index
    r :  end index
    x :  pivot value
--
This is a Python function that implements the Quickselect algorithm to find the kth smallest element in an array 'arr' in the range from index 'l' to 'r'. The 'partition2' function is used to partition the array around a pivot element.

The function first checks if 'k' is smaller than the number of elements in the array. If it is, the function partitions the array using the 'partition2' function and gets the position of the pivot element in the sorted array.

If the position of the pivot element is equal to 'k - 1', the pivot element is returned as it is the kth smallest element.

If the position is more, the function recurs for the left subarray as the kth smallest element is expected to be there. If not, it recurs for the right subarray.

If 'k' is not smaller than the number of elements in the array, the function prints "Index out of bound".    
    
    
    '''
    # if k is smaller than number of elements in array
    if (k > 0 and k <= r - l + 1):
        # Partition the array around last element and get position of pivot element in sorted array
        index = partition2(arr, l, r,r)
        # if position is same as k
        if (index - l == k - 1):
            return arr[index]
        
        # If position is more, recur for left subarray
        if (index - l > k - 1):
            return selectkthSmallest(arr, l, index - 1, k)
        # Else recur for right subarray
        return selectkthSmallest(arr, index + 1, r, k - index + l - 1)
    print("Index out of bound")

def Qmedian_of_medians5(arr, rank):
      return median_of_medians5(arr, rank)


def median_of_medians5(arr, rank):
    
 '''
The code calculates the median of a list of numbers (arr) 
using the median of medians algorithm. The function splits 
the input list into sublists of size 5, calculates the median 
of each sublist, and then calculates the median of those medians
 as the pivot value. It splits the original list into two parts 
 based on the pivot, and then recursively applies the same process 
 to either the lower or upper part, depending on the rank of the 
 target score. If the number of elements in the list is less than 
 or equal to 5, it sorts the list and returns the element at the rank-th
 position.
'''
        # If the number of scores is less than or equal to 5, sort the scores and return the score at the rank-th position
 if len(arr) <= 5:
            arr.sort()
            return arr[rank-1]

        # Split the scores into sublists of size 5
        
 sublists = [arr[i:i+5] for i in range(0, len(arr),5)]
        
        # Find the median of each sublist
 medians = [median_of_medians5(sublist, int(len(sublist)/2)) for sublist in sublists]
        
        # Find the median of the medians
 pivot = median_of_medians5(medians, int(len(medians)/2))

        # Split the scores into two parts: the lower scores and the upper scores
 lower = [x for x in arr if x < pivot]
 upper = [x for x in arr if x > pivot]

        # Recursively apply the median_of_medians function to the lower scores or the upper scores,
        # depending on the rank of the target score
 if rank <= len(lower):
            return median_of_medians5(lower, rank)
 elif rank > len(arr) - len(upper):
            return median_of_medians5(upper, rank - (len(arr) - len(upper)))
 else:
  return pivot

def Qmedian_of_medians3(arr, rank):
      return median_of_medians3(arr, rank)
def median_of_medians3(arr, rank):
        # If the number of scores is less than or equal to 5, sort the scores and return the score at the rank-th position 
        if len(arr) <= 3:
            arr.sort()
            return arr[rank-1]

        # Split the scores into sublists of size 5
        sublists = [arr[i:i+3] for i in range(0, len(arr),3)]
        
        # Find the median of each sublist
        medians = [median_of_medians3(sublist, int(len(sublist)/2)) for sublist in sublists] 
        # Find the median of the medians
        pivot = median_of_medians3(medians, int(len(medians)/2))

        # Split the scores into two parts: the lower scores and the upper scores
        lower = [x for x in arr if x < pivot]
        upper = [x for x in arr if x > pivot]

        # Recursively apply the median_of_medians function to the lower scores or the upper scores,
        # depending on the rank of the target score
        if rank <= len(lower):
            return median_of_medians3(lower, rank)
        elif rank > len(arr) - len(upper):
         return median_of_medians3(upper, rank - (len(arr) - len(upper)))
        else:
            return pivot

            return pivot
        
def Qmedian_of_medians7(arr, rank):
      return median_of_medians7(arr, rank)
def median_of_medians7(arr, rank):
        # If the number of scores is less than or equal to 5, sort the scores and return the score at the rank-th position
        if len(arr) <= 7:
            arr.sort()
            return arr[rank-1]

        # Split the scores into sublists of size 5
        sublists = [arr[i:i+7] for i in range(0, len(arr),7)]
        
        # Find the median of each sublist
        medians = [median_of_medians7(sublist, int(len(sublist)/2)) for sublist in sublists]
        
        # Find the median of the medians
        pivot = median_of_medians7(medians, int(len(medians)/2))

        # Split the scores into two parts: the lower scores and the upper scores
        lower = [x for x in arr if x < pivot]
        upper = [x for x in arr if x > pivot]

        # Recursively apply the median_of_medians function to the lower scores or the upper scores,
        # depending on the rank of the target score
        if rank <= len(lower):
            return median_of_medians7(lower, rank)
        elif rank > len(arr) - len(upper):
            return median_of_medians7(upper, rank - (len(arr) - len(upper)))
        else:
            return pivot 

def medianOfMedians(arr, l, r, chunkSize):
    

    # Calculate the size of the subarray
    n = r - l + 1
    
    # Base case: if the size of the subarray is less than or equal to chunkSize, sort the subarray and return the median
    if n <= chunkSize:
        arr = sorted(arr[l:r+1])
        return arr[n//2]
    
    # Create a list to store the medians of the subarrays
    medians = []
    
    # Loop through the subarrays
    for i in range(l, r+1, chunkSize):
        # Get the current subarray
        subArr = arr[i:min(i+chunkSize, r+1)]
        
        # Sort the current subarray
        subArr = sorted(subArr)
        
        # Find the median of the current subarray
        median = subArr[len(subArr)//2]
        
        # Add the median to the list of medians
        medians.append(median)
    
    # Use the medians to find a pivot
    pivot = medianOfMedians(medians, 0, len(medians) - 1, chunkSize)
    
    # Find the index of the pivot in the original array
    pivotIndex = arr.index(pivot, l, r+1)
    
    # Partition the original array around the pivot
    pivotIndex = partition2(arr, l, r, pivotIndex)
    
    # Calculate k, the number of elements in the left subarray
    k = pivotIndex - l + 1
    
    # If k is equal to n//2, the pivot is the median
    if k == n//2:
        return arr[pivotIndex]
    # If n//2 is less than k, the median is in the left subarray
    elif n//2 < k:
        return medianOfMedians(arr, l, pivotIndex - 1, chunkSize)
    # If n//2 is greater than k, the median is in the right subarray
    else:
        return medianOfMedians(arr, pivotIndex + 1, r, chunkSize)




        
        
def findMedian(arr, chunkSize):
    return medianOfMedians(arr, 0, len(arr) - 1, chunkSize)


    
    
 # assume that r-p+1 <= 5
def findMedian2(a, p, r):
    L = []
    for i in range(p, r+1):
        L.append(a[i])
    L.sort()
    return L[(r-p+1)//2]
   
    
def KthSmallest5(a, p, r, k):
   
    '''This is an implementation of the QuickSelect algorithm,
    a variation of the QuickSort algorithm, to find the k-th smallest element
    in an array 'a' from index 'p' to index 'r'. 
    It works by dividing the array into groups of 5 elements,
    finding the median of each group, and then finding 
    the median of the medians (medOfmed). T
    he medOfmed is used as a pivot and the array is partitioned 
    around the pivot. The k-th smallest element is then either 
    the pivot or found recursively in the half of the array where 
    the k-th smallest element lies.
   '''

    # divide A into floor(n/5) groups
    # create median array with size floor(n/5) 
    n = r - p + 1
    median = []
    i = 0
    while i < n//5:
        # 5 element can be assigned for each group
        median.append(findMedian2(a, p+5*i, p+5*i+4))
        i += 1
    # if last group has n%5 (remainder) elements
    if i*5 < n:
        median.append(findMedian2(a, p+5*i, p+5*i+(n%5-1)))
        i += 1
    # so, at this time i value means floor(n/5)
    if i == 1:
        # if median has only one elements, the medOfmed should be median[0]
        medOfmed = median[i-1]
    else:
        # reculsively medOfmed can be found. 
        # Because median array is generated each recursion, i value should be shrunk more and more 
        medOfmed = KthSmallest5(median, 0, i-1, i//2)
          
    # at this bottom line, medOfmed can be determined 
    # if we use the pivot as medofmed value, the number of sorted elements can be 3(floor(n/5)/2 - 2)
    q = partition2(a, p, r, medOfmed)
    # i value means medOfmed's rank in a[...] array 
    i = q - p + 1 
    if i == k:
        # if partitioned pivot is the kth Smallest element
        return a[q]
    elif i > k:
        return KthSmallest5(a, p, q-1, k)
    else:
        return KthSmallest5(a, q+1, r, k-i)
    

def QuickSelect5(a, p, r, k):
      return KthSmallest5(a, p, r, k)
def QuickSelect3(a, p, r, k):
        return KthSmallest3(a, p, r, k)
def QuickSelect7(a, p, r, k):
      return KthSmallest7(a, p, r, k)

        
def KthSmallest7(a, p, r, k):
    '''
    This is an implementation of the QuickSelect algorithm,
    a variation of the QuickSort algorithm, to find the k-th smallest element
    in an array 'a' from index 'p' to index 'r'. 
    It works by dividing the array into groups of 7 elements,
    finding the median of each group, and then finding 
    the median of the medians (medOfmed). T
    he medOfmed is used as a pivot and the array is partitioned 
    around the pivot. The k-th smallest element is then either 
    the pivot or found recursively in the half of the array where 
    the k-th smallest element lies.
    '''
    # divide A into floor(n/5) groups
    # create median array with size floor(n/5)
    n = r - p + 1
    median = []
    i = 0
    while i < n//7:
        # 5 element can be assigned for each group
        median.append(findMedian2(a, p+7*i, p+7*i+6))
        i += 1
    # if last group has n%7 (remainder) elements
    if i*7 < n:
        median.append(findMedian2(a, p+7*i, p+7*i+(n%7-1)))
        i += 1
    # so, at this time i value means floor(n/5)
    if i == 1:
        # if median has only one elements, the medOfmed should be median[0]
        medOfmed = median[i-1]
    else:
        # reculsively medOfmed can be found. 
        # Because median array is generated each recursion, i value should be shrunk more and more 
        medOfmed = KthSmallest7(median, 0, i-1, i//2)
    # at this bottom line, medOfmed can be determined 
    # if we use the pivot as medofmed value, the number of sorted elements can be 3(floor(n/5)/2 - 2)
    q = partition2(a, p, r, medOfmed)
    # i value means medOfmed's rank in a[...] array 
    i = q - p + 1 
    if i == k:
        # if partitioned pivot is the kth Smallest element
        return a[q]
    elif i > k:
        return KthSmallest7(a, p, q-1, k)
    else:
        return KthSmallest7(a, q+1, r, k-i)
    
    
    
def KthSmallest3(a, p, r, k):

    '''This is an implementation of the QuickSelect algorithm,
  a variation of the QuickSort algorithm, to find the k-th smallest element
  in an array 'a' from index 'p' to index 'r'. 
  It works by dividing the array into groups of 3 elements,
  finding the median of each group, and then finding 
  the median of the medians (medOfmed). T
  he medOfmed is used as a pivot and the array is partitioned 
  around the pivot. The k-th smallest element is then either 
  the pivot or found recursively in the half of the array where 
  the k-th smallest element lies.
  '''
    # divide A into floor(n/5) groups
    # create median array with size floor(n/5)
    n = r - p + 1
    median = []
    i = 0
    while i < n//3:
        # 5 element can be assigned for each group
        median.append(findMedian2(a, p+3*i, p+3*i+2))
        i += 1
    # if last group has n%7 (remainder) elements
    if i*3 < n:
        median.append(findMedian2(a, p+3*i, p+3*i+(n%3-1)))
        i += 1
    # so, at this time i value means floor(n/5)
    if i == 1:
        # if median has only one elements, the medOfmed should be median[0]
        medOfmed = median[i-1]
    else:
        # reculsively medOfmed can be found. 
        # Because median array is generated each recursion, i value should be shrunk more and more 
        medOfmed = KthSmallest3(median, 0, i-1, i//2)
    # at this bottom line, medOfmed can be determined 
    # if we use the pivot as medofmed value, the number of sorted elements can be 3(floor(n/5)/2 - 2)
    q = partition2(a, p, r, medOfmed)
    # i value means medOfmed's rank in a[...] array 
    i = q - p + 1 
    if i == k:
        # if partitioned pivot is the kth Smallest element
        return a[q]
    elif i > k:
        return KthSmallest3(a, p, q-1, k)
    else:
        return KthSmallest3(a, q+1, r, k-i)
    
    

def quickSort(arr, low, high):
    
    '''
    This is an implementation of the QuickSort algorithm.
    It works by selecting the middle element of the array as the pivot,
    partitioning the array around the pivot, and recursively
    sorting the subarrays to the left and right of the pivot. 
    The base case is when the low index is greater than or equal to 
    the high index, indicating that the subarray has only one element or
    is empty, and thus, does not need to be sorted. The selectkthSmallest() 
    function is used to find the k-th smallest element in the array,
    which is used as the pivot in this case
    
    '''
    # If the low index is less than the high index, continue with the sorting process
    if low < high:
        p=KthSmallest7(arr,low ,high,int((high-low)/2 +1) )
        
        # Partition the array around the pivot element
        pi = partition2(arr, low, high, high)
        
        # Recursively sort the elements in the left subarray
        quickSort(arr, low, pi - 1)
        
        # Recursively sort the elements in the right subarray
        quickSort(arr, pi + 1, high)


#arr=[25,24,33,39,3,18,19,31,23,49,45,16,1,26,40,22,15,20,24,4,13,34]
#a=[10023,100845,12290,12345,3345,22134,1124567,4545,1234,7789,3345,123]
#A = [1,2,3,4,5,1000,8,9,99]

#print(a)
#size=len(a)
#print('Median-finding algorithms')

#rank=int(input('Enter the rank :'))
#print("The data after partition last element with its correct position in index :", partition2(a, 0, size-1, size-1))
#print("The",rank,"kth smallest element O(N) , O(N^2):", selectkthSmallest(a, 0, size-1, rank))


#print('the',rank,'kth smallest element (group 5):',KthSmallest5(a, 0, size-1, rank))

#print('the',rank,'kth smallest element (group 3):',KthSmallest3(a, 0, size-1, rank)) 

#print('the',rank,'kth smallest element (group 7):',KthSmallest7(a, 0, size-1, rank)) 



#print("The median of median QuickSelectMedians :",QuickSelectMedians(a, 0, size-1, rank))

#print('----Median of Median Algorithms----')


#print(" median of median algorithms with group 3: ", median_of_medians3(a,rank))
#print(" median of median algorithms with group 5: ", median_of_medians5(a,rank))
#print(" median of median algorithms with group 7: ", median_of_medians7(a,rank))



#print('---Median of the array----')
#m=medianOfMedians(a, 0, size-1, rank)
#print(m)



#q=quickSort(a, 0, size- 1)

#print("----Sorted array ----", a)