# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 22:31:34 2023

@author: Shaha
"""

import time 
import bst_m
import heap_m
import random_m
import median_m

def readME():
    with open('READ ME ALgorithms .txt') as f:
         lines = f.read()
         print(lines)

def readlist():   
    #opening the file in read mode
    myFile = open("flist.txt","r")
    arr = []
    for number in myFile:
        arr.append(int(number))  
    myFile.close()
    return arr

arr = readlist()
size = len(arr)  

def menu():
    print('\n1- if you want to read the README file \n'+
          '2- use median of medians algorithm \n' +
          '3- use randomized finding median algorithm \n' +
          '4- find the median by using heap \n' +
          '5- find the median by using the binary search \n' +
          ' to exit print 0 \n')
    
def writeList():
    writeCodeIn = open("fSortedlist.txt","w")

    for i in range(size):
        writeCodeIn.write(str(arr[i])+"\n")  
    writeCodeIn.close() 
  
menu()
option = int(input('Enter your choice: '))

while option != 0 :
    #check what choice was entered and act accordingly
    if option == 1: 
        print("THE README FILE ")
        readME()
        menu()
        option = int(input('Enter your choice: '))
    elif option == 2: 
        start = time.process_time()
        rank=int(input('Enter the rank :'))
        print("The data after partition last element with its correct position in index :", median_m.partition2(arr, 0, size-1, size-1))
        print("the time :",time.process_time()-start)
        start = time.process_time()
        print("The",rank,"kth smallest element O(N) , O(N^2):", median_m.selectkthSmallest(arr, 0, size-1, rank))
        print("the time :",time.process_time()-start)
        start = time.process_time()
        print('the',rank,'kth smallest element (group 5):',median_m.QuickSelect5(arr, 0, size-1, rank))
        print("the time :",time.process_time()-start)
        start = time.process_time()
        print('the',rank,'kth smallest element (group 3):',median_m.QuickSelect3(arr, 0, size-1, rank)) 
        print("the time :",time.process_time()-start)
        start = time.process_time()
        print('the',rank,'kth smallest element (group 7):',median_m.QuickSelect7(arr, 0, size-1, rank)) 
        print("the time :",time.process_time()-start)
        
        print('----Median of Median Algorithms----')
        start = time.process_time()
        print(" median of median algorithms with group 3: ",median_m. Qmedian_of_medians3(arr,rank))
        print("the time :",time.process_time()-start)
        start = time.process_time()
        print(" median of median algorithms with group 5: ",median_m. Qmedian_of_medians5(arr,rank))
        print("the time :",time.process_time()-start)
        start = time.process_time()
        print(" median of median algorithms with group 7: ",median_m. Qmedian_of_medians7(arr,rank)) 
        print("the time :",time.process_time()-start)
        
        start = time.process_time()
        q=median_m.quickSort(arr, 0, size- 1)
        print("----Sorted array ----", arr)
        print("the time :",time.process_time()-start)
    
        
        
        
        menu()
        option = int(input('Enter your choice: '))
        
    elif option == 3:      
         start = time.process_time()
         rank=int(input('Enter the rank :'))
         print("The",rank,"kth smallest element :", random_m.selectkthSmallestrand(arr, 0, size-1, rank))
         print("the time :",time.process_time()-start)
         start = time.process_time()
         print('the',rank,'kth smallest element (random):',random_m.KthSmallestRandomized(arr, 0, size-1, rank))
         print("the time :",time.process_time()-start)

         print('----Median of Median Algorithms----')

         start = time.process_time()
         print(" median of median algorithms with group 3: ", random_m.median_of_medians3rand(arr,rank))
         print("the time :",time.process_time()-start)
         start = time.process_time()
         print(" median of median algorithms with group 5: ", random_m.median_of_medians5rand(arr,rank))
         print("the time :",time.process_time()-start)
         start = time.process_time()
         print(" median of median algorithms with group 7: ", random_m.median_of_medians7rand(arr,rank))
         print("the time :",time.process_time()-start)
         start = time.process_time()
         q=random_m.quickSort(arr, 0, size- 1)
         print("----Sorted array ----", arr)
         print("the time :",time.process_time()-start)
         

         writeList()
        
         menu()
         option = int(input('Enter your choice: '))
        
    elif option == 4:        
         rank=int(input('Enter the rank :'))
         start = time.process_time()
         print("The kth smallest element is:",heap_m.kthSmallest(arr,rank))
         print("the time :",time.process_time()-start)
         start = time.process_time()
         print(" median of median algorithms with group 3: ", random_m.median_of_medians3rand(arr,rank))
         print("the time :",time.process_time()-start)
         start = time.process_time()
         print(" median of median algorithms with group 5: ", random_m.median_of_medians5rand(arr,rank))
         print("the time :",time.process_time()-start)
         start = time.process_time()
         print(" median of median algorithms with group 7: ", random_m.median_of_medians7rand(arr,rank))
         print("the time :",time.process_time()-start)
         
         writeList()
        
         menu()
         option = int(input('Enter your choice: '))
        
    elif option == 5:       
         
         rank=int(input('Enter the rank :'))
         bst =bst_m.BST()
         for number in arr:
             bst.insert(number)
         cnt = [0]
         start = time.process_time()
         bst.kthSmallest(bst.root, rank, cnt)
         print("the time :",time.process_time()-start)
         writeList()
         menu()
         option = int(input('Enter your choice: ')) 
        
    else:
        print ('Invalid option. please enter a number between 0 and 4')
        menu()
        option = int(input('Enter your choice: '))
        
