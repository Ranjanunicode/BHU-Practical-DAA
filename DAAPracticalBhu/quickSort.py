# 5. Write a program to implement Quick Sort algorithm.
# Also plot the graph of the time complexity for different values of array size ‘n’.

## Quick Sort ###########################

import time
import numpy as np
import matplotlib.pyplot as plt


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
    newArr = []
    if low < high:
        # pi is partitioning index, arr[p] is now at right place
        pi = partition(arr, low, high)
        # Separately sort elements before partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)


def plot(t):
    nsq = []
    n = []
    for i in range(1, 31):
        n.append((i*1000))
    # print(n)
    # n = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    newArr = []
    for i in range(len(n)):
        arr = n[i]*np.log2(n[i]) / 10**5.8
        # nsq.append(n[i] * n[i] * 10)
        # arr_nsq = n[i] * n[i]
        newArr.append(arr)
    # plotting the points
    plt.plot(n, t, label="Quick Sort")
    plt.plot(n, newArr, label="nlogn")
    # plt.plot(n, nsq, label="n^2")
    plt.xlabel('No. of inputs')
    plt.ylabel('Total time taken')

    # giving a title to my graph
    plt.title('Quick Sort analysis')
    plt.legend()
    # function to show the plot
    plt.show()


# main function
if __name__ == "__main__":
    tval = []
    for i in range(2):
        randarr1 = np.random.randint(1, 100, 20)
        print(f"Random generated array : {randarr1}")
        quickSort(randarr1, 0, len(randarr1)-1)
        sorted = randarr1
        print(f"Sorted array : {sorted}")

    for i in range(1, 31):
        randarr = np.random.randint(1, 200, i*1000)
        # print(randarr)
        n = len(randarr)
        start_time = time.perf_counter()
        result = quickSort(randarr, 0, n-1)
        timeTaken = (time.perf_counter() - start_time)
        tval.append(timeTaken)
        # print(timeTaken, end=" Nano-seconds\n")
    # print(tval)
    plot(tval)
