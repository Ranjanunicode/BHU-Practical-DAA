# 6. Write a program to implement Counting Sort algorithm.
# Also plot the graph of the time complexity for different values of array size ‘n’.

## Counting Sort ########################

import time
import numpy as np
import matplotlib.pyplot as plt


def countingSort(array):
    size = len(array)
    output = [0] * size
    m = max(array)
    count = [0] * m
    for i in range(0, size):
        count[array[i]] += 1

    # Store the cummulative count
    for i in range(len(array)):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, size):
        array[i] = output[i]


def plot(t):
    nsq = []
    n = []
    for i in range(1, 31):
        n.append((i*1000))
    # n = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, ...]
    newArr = []
    narr = []
    for i in range(len(n)):
        arr = n[i]*np.log2(n[i]) / 10**6
        arrn = n[i] / 10**6
        narr.append(arrn)
        newArr.append(arr)

    plt.plot(n, t, label="Counting Sort")
    # plt.plot(n, newArr, label="nlogn")
    plt.plot(n, narr, label="n")
    plt.xlabel('No. of inputs')
    plt.ylabel('Total time taken')
    plt.title('Counting Sort analysis')
    plt.legend()
    plt.show()


# main function
if __name__ == "__main__":
    for i in range(2):
        randarr1 = np.random.randint(1, 100, 20)
        print(f"Random generated array : {randarr1}")
        countingSort(randarr1)
        sorted = randarr1
        print(f"Sorted array : {sorted}")

    tval = []
    for i in range(1, 31):
        randarr = np.random.randint(1, 200, i*1000)
        n = len(randarr)
        start_time = time.perf_counter()
        countingSort(randarr)
        timeTaken = (time.perf_counter() - start_time)
        tval.append(timeTaken)
        # print(timeTaken, end=" Nano-seconds\n")
    # print(tval)
    plot(tval)
