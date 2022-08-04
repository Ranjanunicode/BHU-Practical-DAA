import time
import numpy as np
import matplotlib.pyplot as plt

#########################################
## Selection Sort #######################


def selectionSort(alist):

    for i in range(len(alist)):

       # Find the minimum element in remaining
        minPosition = i

        for j in range(i+1, len(alist)):
            if alist[minPosition] > alist[j]:
                minPosition = j

        # Swap the found minimum element with minPosition
        temp = alist[i]
        alist[i] = alist[minPosition]
        alist[minPosition] = temp
#########################################

#########################################
## Insertion Sort #######################


def insertionSort(arr):

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
#########################################

#########################################
## Merge Sort ###########################


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# l is for left index and r is right index of the
# sub-array of arr to be sorted


def mergeSort(arr, l, r):
    if l < r:
        # Same as (l+r)/2, but avoids overflow for
        # large l and h
        m = l + (r-l)//2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
#########################################

#########################################
## Quick Sort ###########################


def partition(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:

            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

# Function to do Quick sort


def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
#########################################

#########################################
## Counting Sort ########################


def countingSort(array1):
    max_val = max(array1)
    m = max_val + 1
    count = [0] * m

    for a in array1:
        # count occurences
        count[a] += 1
    i = 0
    for a in range(m):
        for c in range(count[a]):
            array1[i] = a
            i += 1
#########################################
#########################################
## Radix Sort ########################


# Python program for implementation of Radix Sort
# A function to do counting sort of arr[] according to
# the digit represented by exp.

def countingSortR(arr, exp1):

    n = len(arr)

    # The output array elements that will have sorted arr
    output = [0] * (n)

    # initialize count array as 0
    count = [0] * (10)

    # Store count of occurrences in count[]
    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]

# Method to do Radix Sort


def radixSort(arr):

    # Find the maximum number to know number of digits
    max1 = max(arr)

    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 / exp > 1:
        countingSortR(arr, exp)
        exp *= 10

#########################################
#########################################
## Heap Sort ########################


# Python program for implementation of

# To heapify subtree rooted at index i.
# n is size of heap


def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1	 # left = 2*i + 1
    r = 2 * i + 2	 # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[largest] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)

# The main function to sort an array of given size


def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

#########################################


#########################################
## Main #################################
sorts = [
    # {
    #     "name": "Selection Sort",
    #     "sort": lambda arr: selectionSort(arr)
    # },
    {
        "name": "Radix Sort",
        "sort": lambda arr: radixSort(arr)
    },
    # {
    #     "name": "Heap Sort",
    #     "sort": lambda arr: heapSort(arr)
    # },
    # {
    #     "name": "Insertion Sort",
    #     "sort": lambda arr: insertionSort(arr)
    # },
    {
        "name": "Counting Sort",
        "sort": lambda arr: countingSort(arr)
    },
    # {
    #     "name": "Merge Sort",
    #     "sort": lambda arr: mergeSort(arr, 0, len(arr) - 1)
    # },
    # {
    #     "name": "Quick Sort",
    #     "sort": lambda arr: quickSort(arr, 0, len(arr) - 1)
    # },
]

elements = np.array([i*1000 for i in range(1, 11)])

plt.xlabel('List Length')
plt.ylabel('Time Complexity')

for sort in sorts:
    times = list()
    # start_all = time.time()
    for i in range(1, 11):
        start = time.time()
        a = np.random.randint(1000, size=i * 1000)

        sort["sort"](a)
        end = time.time()
        times.append(end - start)
        print(sort["name"], "Sorted", i * 1000,
              "Elements in", end - start, "s")
    end_all = time.time()
    # print(sort["name"], "Sorted Elements in", "s")

    plt.plot(elements, times, label=sort["name"])


plt.grid()
plt.legend()
plt.show()
