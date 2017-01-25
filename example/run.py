# You can do all of this in the `__main__.py` file, but this file exists
# to shows how to do relative import functions from another python file in
# the same directory as this one.
import numpy as np
from .algs import quicksort, bubblesort
from timeit import default_timer as timer
import matplotlib.pyplot as plt


# All plotting was done within the run_stuff function, so it was called when the example module was run through the command line


def run_stuff():
    """
    This function is called in `__main__.py`
    """
    print("This is `run()` from ", __file__)

    x = np.random.rand(10)
    print("Unsorted input: ", x)

    print("Bubble sort output: ", bubblesort(x))
    print("Quick sort output: ", quicksort(x, 0, len(x) - 1))
    
    
    
    # Test time complexity of bubblesort
    # Create 10 arrays each of sizes 100, 200, ...1000
    # Time the sorting of each array, store in a new array
    
    bubblesorttime = np.zeros((10,10)) # array to store all times
#    bubbleassign = np.zeros((10,10)) # store assignment counts
#    bubblecondition = np.zeros((10,10))
    for i in range(1,11): # make arrays of length 100, 200, ... 1000 
        for j in range(1,11): # make 10 arrays of each length
            testtime = np.random.rand(i*100)
            start = timer() # get time at start of the run
#            bubblesortarray, condition, assign = bubblesort(testtime) # call bubblesort on the random array, use this when counting assignements and condtionals
            bubblesort(testtime) # call bubblesort on the random array
            end = timer() # get time at end of the run
            elapsed = end - start # elapsed time to run the function
            bubblesorttime[i-1,j-1] = elapsed # store time of each run
#            bubblecondition[i-1,j-1] = condition
#            bubbleassign[i-1,j-1] = assign
    
    # Calculate the mean time of each row (for each array length)        
    meantimesbubble = np.mean(bubblesorttime, axis = 1) 
#    meancondition = np.mean(bubblecondition, axis = 1)
#    meanassign = np.mean(bubbleassign, axis = 1)
    plt.figure(1)
    xvals = np.array(range(100,1100,100))      
    plt.plot(xvals, meantimesbubble, label = 'Bubblesort')
    plt.xlabel('Length of array')
    plt.ylabel('Average time to sort array (s)')
    plt.title('Time complexity of two sorting algorithms')
    
    # Fit a curve to bubblesort results and plot
    bubblefit = np.polyfit(xvals, meantimesbubble, 2) # coefficients of n^2
    yvalsfit = bubblefit[0]*xvals**2 + bubblefit[1]*xvals + bubblefit[2]
          
    plt.plot(xvals, meantimesbubble, 'bo', label = 'Bubblesort')
    plt.plot(xvals, yvalsfit, ':', label = 'O(n^2)')
    
    plt.xlabel('Length of array')
    plt.ylabel('Average time to sort array (s)')
    plt.title('Time complexity of Bubblesort')
    plt.legend()
    
    # Plot assignments and condtionals
#    plt.figure(2)
#    plt.plot(xvals, meancondition, label = ('Bubblesort conditionals'))
#    plt.plot(xvals, meanassign, label = ('Bubblesort assignments'))
#    plt.legend()
#    plt.xlabel('Length of array')
#    plt.ylabel('Number of conditionals or assignments')
#    plt.title('Bubblesort count of conditionals and assignments')
#    plt.savefig('BubblesortConditionAssign')
    
    
    
    # Test time complexity of quicksort
    # Create 10 arrays each of sizes 100, 200, ...1000
    # Time the sorting of each array, store in a new array
        
    quicksorttime = np.zeros((10,10)) # array to store all times
#    quickassign = np.zeros((10,10)) # store assignment counts
#    quickcondition = np.zeros((10,10))
    for i in range(1,11): # make arrays of length 100, 200, ... 1000 
        for j in range(1,11): # make 10 arrays of each length
            testtime = np.random.rand(i*100)
            start = timer() # get time at start of the run
#            quicksortarray, condition, assign = quicksort(testtime, 0, len(testtime) - 1) # use this when counting assignments and conditionals
            quicksort(testtime, 0, len(testtime) - 1) # call quicksort on random array
            end = timer() # get time at end of the run
            elapsed = end - start # time to run the function
            quicksorttime[i-1,j-1] = elapsed # store time of each run
#            quickcondition[i-1,j-1] = condition
#            quickassign[i-1,j-1] = assign
    
    # Calculate the mean time of each row (for each array length)        
    meantimesquick = np.mean(quicksorttime, axis = 1)
#    meancondition = np.mean(quickcondition, axis = 1)
#    meanassign = np.mean(quickassign, axis = 1)
    plt.figure(2)       
    plt.plot(xvals, meantimesquick, label = 'Quicksort')
    yvalsnlogn = np.multiply(xvals, np.log10(xvals)) # Compare quicksort to O(nlogn)
    plt.plot(xvals, yvalsnlogn, ':', label = 'O(nlogn)')
    plt.legend()
    #plt.savefig('BubbleQuickPlot')
    plt.show()
    plt.xlabel('length of array')
    plt.ylabel('average time to sort array (s)')
    plt.title('Quicksort time complexity')
    
#    # Plot assignments and condtionals
#    plt.figure(2)
#    plt.plot(xvals, meancondition, label = ('Quicksort conditionals'))
#    plt.plot(xvals, meanassign, label = ('Quicksort assignments'))
#    plt.legend()
#    plt.xlabel('Length of array')
#    plt.ylabel('Number of conditionals or assignments')
#    plt.title('Quicksort count of conditionals and assignments')
#    plt.savefig('QuicksortConditionAssign')
#    plt.show()
    
    # Compare time complexity to worst case
    #plt.figure(2)
    #plt.plot(xvals, yvalsnlogn, label = 'O(nlogn)')
    #plt.plot(xvals, meantimesquick, label = 'Quicksort')
    #plt.legend()
    #plt.xlabel('Length of array')
    #plt.ylabel('Average time to sort array (s)')
    #plt.title('Time complexity of Quicksort')
    #
    #plt.figure(3)
    #plt.plot(xvals, yvalsn2, label = 'O(n^2)')
    #plt.plot(xvals, meantimesbubble, label = 'Bubblesort')
    #plt.legend()
    #plt.xlabel('Length of array')
    #plt.ylabel('Average time to sort array (s)')
    #plt.title('Time complexity of Bubblesort')
