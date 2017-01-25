import numpy as np
from example import algs
import timeit
import matplotlib.pyplot as plt

def test_pointless_sort():
    # generate random vector of length 10
    x = np.random.rand(10)

    # check that pointless_sort always returns [1,2,3]
    assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))

    # generate a new random vector of length 10
    x = np.random.rand(10)

    # check that pointless_sort still returns [1,2,3]
    assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))

def test_bubblesort():
    # Actually test bubblesort here. It might be useful to think about
    # some edge cases for your code, where it might fail. Some things to
    # think about: (1) does your code handle 0-element arrays without
    # failing, (2) does your code handle characters?

    x = np.array([1,2,4,0,1])
    
#    # for now, just attempt to call the bubblesort function, should
#    # actually check output
#    algs.bubblesort(x)
    assert np.array_equal(algs.bubblesort(x), np.array([0,1,1,2,4]))
    
    # Test 1: given an empty vector, bubblesort returns an empty vector
    testempty = np.array([])
    assert np.array_equal(algs.bubblesort(testempty), np.array([]))
    
    # Test 2: given a single element vector, bubblesort returns the same single
    # element vector.
    testsingle = np.array([3])
    assert np.array_equal(algs.bubblesort(testsingle), np.array([3]))

    # Test 3: given duplicated elements, bubblesort returns sorted elements
    testduplicated = np.array([3,2,5,5,7,2,3])
    assert np.array_equal(algs.bubblesort(testduplicated), np.array([2,2,3,3,5,5,7]))
    
    # Test 4: test vector of odd input length
    testodd = np.array([8,2,5,6,1])
    assert np.array_equal(algs.bubblesort(testodd), np.array([1,2,5,6,8]))
    
    # Test 5: test vector of even input length
    testeven = np.array([8,2,6,1])
    assert np.array_equal(algs.bubblesort(testeven), np.array([1,2,6,8]))
    
    # Test 6: given a vector of characters, bubblesort sorts alphabetically
    testchar = np.array(['n', 'x', 'a', 'q'])
    assert np.array_equal(algs.bubblesort(testchar), np.array(['a','n','q','x']))
    
    # Test 7: given a vector that is already sorted, return the same vector
    testsorted = np.array([1,3,4,5,6])
    assert np.array_equal(algs.bubblesort(testsorted), np.array([1,3,4,5,6]))
    
    # Test time complexity of bubblesort
    # Create 10 arrays each of sizes 100, 200, ...1000
    # Time the sorting of each array, store in a new array
    
    bubblesorttime = np.zeros((10,10))
    for i in range(1,11): # make arrays of length 100, 200, ... 1000 
        for j in range(1,11): # make 10 arrays of each length
            testtime = np.random.rand(i*10)
            start = timeit.timeit() # get time at start of the run
            algs.bubblesort(testtime)
            end = timeit.timeit() # get time at end of the run
            elapsed = end - start # time to run the function
            bubblesorttime[i-1,j-1] = elapsed # store time of each run
    
    # Calculate the mean time of each row (for each array length)        
    meantimes = np.mean(bubblesorttime, axis = 1)       
    plt.plot(range(100,1100, 100), meantimes)

def test_quicksort():

    x = np.array([1,2,4,0,1])
    # for now, just attempt to call the quicksort function, should
    # actually check output
    algs.quicksort(x, 0, len(x) - 1)
    
    y = np.array([2,1,3])
    assert np.array_equal(algs.quicksort(y, 0, len(y) - 1), np.array([1,2,3]))
    
    # Test 1: given an empty vector, quicksort returns an empty vector
    testempty = np.array([])
    assert np.array_equal(algs.quicksort(testempty, 0, len(testempty) - 1), np.array([]))
    
    # Test 2: given a single element vector, quicksort returns the same single
    # element vector.
    testsingle = np.array([3])
    assert np.array_equal(algs.quicksort(testsingle, 0, len(testsingle) - 1), np.array([3]))

    # Test 3: given duplicated elements, quicksort returns sorted elements
    testduplicated = np.array([3,2,5,5,7,2,3])
    assert np.array_equal(algs.quicksort(testduplicated, 0, len(testduplicated) - 1), np.array([2,2,3,3,5,5,7]))
    
    # Test 4: test vector of odd input length
    testodd = np.array([8,2,5,6,1])
    assert np.array_equal(algs.quicksort(testodd, 0, len(testodd) - 1), np.array([1,2,5,6,8]))
    
    # Test 5: test vector of even input length
    testeven = np.array([8,2,6,1])
    assert np.array_equal(algs.quicksort(testeven, 0, len(testeven) -1), np.array([1,2,6,8]))
    
    # Test 6: given a vector of characters, bubblesort sorts alphabetically
    testchar = np.array(['n', 'x', 'a', 'q'])
    assert np.array_equal(algs.quicksort(testchar, 0, len(testchar) - 1), np.array(['a','n','q','x']))
    
    # Test 7: given a vector that is already sorted, return the same vector
    testsorted = np.array([1,3,4,5,6])
    assert np.array_equal(algs.quicksort(testsorted, 0, len(testsorted) -1), np.array([1,3,4,5,6]))
