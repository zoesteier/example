## Algs contains pointless sort, bubblesort, and quicksort functions
## Zoë Steier, 1/24/17, BMI 203
#

import numpy as np

def pointless_sort(x):
    """
    This function always returns the same values to show how testing
    works, check out the `test/test_alg.py` file to see.
    """
    return np.array([1,2,3])

def bubblesort(x):
    """
    Describe how you are sorting `x`:
        Iterate through list of numbers. If two adjacent numbers are misordered, 
        swap the pair so the smaller number comes first. Continue iterating 
        through the list until all numbers are aligned.
    """

    for j in range(len(x)): # repeat inner loop once for each element (worst case)
        for i in range(1, len(x) - j): # for each element in x in unsorted section,
            # since each inner loop will move next largest element to the end
            
            if x[i] < x[i-1]: # First conditional
                placeholder = x[i-1] # First assignment
                x[i-1] = x[i] # Second assignment
                x[i] = placeholder # Third assignment

    return x
#
##x = np.random.rand(10)
##print("Unsorted input: ", x)
##print("Bubble sort output: ", bubblesort(x))    
# 


### The quicksort algorithm includes the quicksort funciton and the helper function called partition

   
def partition(x, start, end):
    """ This function is a helper function for quicksort. It finds the index of
    the partition (i.e. where to split the array so that the subarray on the 
    left is lower than the pivot and the subarray on the right is greater than 
    the pivot).
    """    
    pivot = x[end] # Choose the last element of the array to be the pivot
    # Second assignment
    
    pindex = start # Initialize the partition index at the beginning of the subarray
    # Third assignment
    
    for i in range(start, end): # Iterate through each element in the subarray
        if x[i] <= pivot: # Second conditional
            x[i], x[pindex] = x[pindex], x[i] # Swap the current element with 
            # the element at the partition index to move smaller numbers to the
            # left of the partition, 
            # Fourth assignment
            
            pindex += 1 # Increment the partition index (one to the right of the swap),
            # Fifth assignment
            
    x[pindex], x[end] = x[end], x[pindex] # Move the pivot element from the end
    # to its correct spot at the partition
    # Sixth assignment
    
    return pindex # The partition index is the index of the number used as the pivot
    # i.e. where the array is divided so numbers to the left are lower and numbers 
    # to the right are higher
 
    
def quicksort(x, start, end):
    """
    Describe how you are sorting `x`:
        Partition the array into two smaller arrays where everything in the left
        subarray is less than some number (the pivot) and everything in the 
        right array is greater than the pivot. Then recursively call
        quicksort on th two smaller arrays until the base case (array size of one)
        is reached, at which point the entire array will be sorted.
        
    """
    # Termination condition: if the array length is one or if the array is invalid
    # (i.e. start > end), output the array
    if start >= end: # First conditional
        return x 
        
    pindex = partition(x, start, end) # Find the partition index, # First assignment
    quicksort(x, start, pindex - 1) # Recursively call quicksort on the subarray
    # to the left of the partition i.e. all numbers smaller than the pivot
    quicksort(x, pindex + 1, end) # Recursively call quicksort on the subarray
    # to the left of the partition i.e. all numbers smaller than the pivot

    return x # x is the sorted array

######################################################### 
####################### Counting
############################################################

#def bubblesort(x):
#    """
#    Describe how you are sorting `x`:
#        Iterate through list of numbers. If two adjacent numbers are misordered, 
#        swap the pair so the smaller number comes first. Continue iterating 
#        through the list until all numbers are aligned.
#    """
#    assignments = 0 # initialize count of assignments
#    conditionals = 0 # initialize count of conditionals
#    for j in range(len(x)): # repeat inner loop once for each element (worst case)
#        for i in range(1, len(x) - j): # for each element in x in unsorted section,
#            # since each inner loop will move next largest element to the end
#            
#            conditionals += 1
#            if x[i] < x[i-1]: # First conditional
#                placeholder = x[i-1] # First assignment
#                x[i-1] = x[i] # Second assignment
#                x[i] = placeholder # Third assignment
#                assignments += 3
##    print('assignments: ', assignments)
##    print('conditionals: ', conditionals)
#
#    return x, conditionals, assignments

#def partition(x, start, end):
#    """ This function is a helper function for quicksort. It finds the index of
#    the partition (i.e. where to split the array so that the subarray on the 
#    left is lower than the pivot and the subarray on the right is greater than 
#    the pivot).
#    """    
#    
#    
#    cpart = 0 # initialize conditions in partition
#    apart = 0 # initialize assignments in partition
#    
#    pivot = x[end] # Choose the last element of the array to be the pivot
#    # Second assignment
#    apart += 1
#    
#    
#    pindex = start # Initialize the partition index at the beginning of the subarray
#    # Third assignment
#    apart += 1
#    
#    for i in range(start, end): # Iterate through each element in the subarray
#        cpart += 1
#        if x[i] <= pivot: # Second conditional
#            x[i], x[pindex] = x[pindex], x[i] # Swap the current element with 
#            # the element at the partition index to move smaller numbers to the
#            # left of the partition, 
#            # Fourth assignment
#            apart += 1
#            
#            pindex += 1 # Increment the partition index (one to the right of the swap),
#            # Fifth assignment
#            apart += 1
#            
#    x[pindex], x[end] = x[end], x[pindex] # Move the pivot element from the end
#    # to its correct spot at the partition
#    # Sixth assignment
#    apart += 1
#    
#    #partitionoutput = (pindex, cpart, apart) 
#    
#    return pindex, cpart, apart # The partition index is the index of the number used as the pivot
#    # i.e. where the array is divided so numbers to the left are lower and numbers 
#    # to the right are higher
#
#
#def quicksort(x, start, end):
#    """
#    Describe how you are sorting `x`:
#        Partition the array into two smaller arrays where everything in the left
#        subarray is less than some number (the pivot) and everything in the 
#        right array is greater than the pivot. Then recursively call
#        quicksort on th two smaller arrays until the base case (array size of one)
#        is reached, at which point the entire array will be sorted.
#        
#    """
#    # Termination condition: if the array length is one or if the array is invalid
#    # (i.e. start > end), output the array
#    
#    conditionals = 0
#    assignments = 0
##    conditionals = 0 # initialize conditionals in outer function
##    assignments = 0 # initialize assignments in outer function
##    cquick = 0 # initialize conditionals in each call of quicksort
##    aquick = 0 # initialize assignments in each call of quicksort
#
#    
#    if start >= end: # First conditional
#        conditionals += 1
#        return x, conditionals, assignments
#        
#    pindex, cpart, apart = partition(x, start, end) # Find the partition index, conditionals, and assignments in the partition function # First assignment
#    conditionals += cpart
#    assignments += apart
#    
#    x, cquick, aquick = quicksort(x, start, pindex - 1) # Recursively call quicksort on the subarray
#    # to the left of the partition i.e. all numbers smaller than the pivot
#    conditionals += cquick
#    assignments += aquick
#    x, cquick, aquick = quicksort(x, pindex + 1, end) # Recursively call quicksort on the subarray
#    conditionals += cquick
#    assignments += aquick
#    # to the left of the partition i.e. all numbers smaller than the pivot
#    
##    conditionals += cpart + cquickl + cquickr
##    assignments += apart + aquickl + aquickr
#    
#    return x, conditionals, assignments # x is the sorted array
#
##x = np.random.rand(10)
##print("Unsorted input: ", x)
##print("Quick sort output: ", quicksort(x, 0, len(x) - 1))