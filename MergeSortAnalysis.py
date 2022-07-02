# 1. Write a program to implement Merge Sort algorithm.
# Also plot the graph of the time complexity for different values of array size ‘n’.
import time
import numpy as np
import matplotlib.pyplot as plt


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
        
    i = 0	
    j = 0	 
    k = l	 

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


# sub-array of arr to be sorted
def mergeSort(arr, l, r):
    if l < r:

        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)


def plot(t):
    nsq = []
    n = []
    for i in range(1, 41):
        n.append((i*1000))
    # print(n)
    # n = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    newArr = []
    for i in range(len(n)):
        arr = n[i]*np.log2(n[i]) / 10**5.4
        # nsq.append(n[i] * n[i] * 10)
        # arr_nsq = n[i] * n[i]
        newArr.append(arr)

    # plotting the points
    plt.plot(n, t, label="merge sort")
    plt.plot(n, newArr, label="nlogn")
    # plt.plot(n, nsq, label="n^2")
    plt.xlabel('No. of inputs')
    plt.ylabel('Total time taken')

    # giving a title to my graph
    plt.title('Merge Sort analysis')
    plt.legend()
    # function to show the plot
    plt.show()

# main function
if __name__ == '__main__':
    tval = []
    for i in range(1, 41):
        randarr = np.random.randint(1, 200, i*1000)
        n = len(randarr)
        start_time = time.perf_counter()
        mergeSort(randarr, 0, n-1)
        timeTaken = (time.perf_counter() - start_time)
        tval.append(timeTaken)
    # print(tval)
    plot(tval)
