# Write a program to implement Merge Sort algorithm.
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

    # Merge the temp arrays back into arr[l..r]
    i = 0	 # Initial index of first subarray
    j = 0	 # Initial index of second subarray
    k = l	 # Initial index of merged subarray

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
    for i in range(1, 21):
        n.append((i*100))
    # print(n)
    # n = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    newArr = []
    for i in range(len(n)):
        arr = n[i]*np.log2(i) * 10**4 / 3
        nsq.append(n[i] * n[i] * 10)
        # arr_nsq = n[i] * n[i]
        newArr.append(arr)

    # plotting the points
    plt.plot(n, t, label="merge sort")
    plt.plot(n, newArr, label="nlogn")
    # plt.plot(n, nsq, label="n^2")
    # naming the x axis
    plt.xlabel('No. of inputs')
    # naming the y axis
    plt.ylabel('Total time taken')

    # giving a title to my graph
    plt.title('Merge Sort analysis')
    plt.legend()
    # function to show the plot
    plt.show()


if __name__ == '__main__':
    tval = []
    for i in range(1, 21):
        randarr = np.random.randint(1, 200, i*100)
        # print(randarr)
        # print(nvarr)

        n = len(randarr)
        print(n, end=" elements\n")
        # print("Given array is")
        # for i in range(n):
        #     print("%d" % randarr[i], end=" ")
        start_time = time.perf_counter_ns()
        mergeSort(randarr, 0, n-1)
        timeTaken = (time.perf_counter_ns() - start_time)
        tval.append(timeTaken)
        # print("\n\nSorted array is")
        # for i in range(n):
        #     print("%d" % randarr[i], end=" ")
        # print("\n")

        print(timeTaken, end=" Nano-seconds\n")
    print(tval)
    plot(tval)
