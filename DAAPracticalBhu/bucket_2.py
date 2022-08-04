#  7.     Write a program to implement the Bucket sort algorithm.
#  Verify that it runs in linear time for inputs coming from a uniform distribution.

## Bucket Sort ########################

import matplotlib.pyplot as plt
import numpy as np
import time


def insertionSort(b):
    for i in range(1, len(b)):
        up = b[i]
        j = i - 1
        while j >= 0 and b[j] > up:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = up
    return b


def BucketSort(x):
    arr = []
    slot_num = len(x)  # 10 means 10 slots, each
    # slot's size is 0.1
    for i in range(slot_num):
        arr.append([])

    # Put array elements in different buckets
    for j in x:
        index_b = int(slot_num * j)
        arr[index_b].append(j)

    # Sort individual buckets
    for i in range(slot_num):
        arr[i] = insertionSort(arr[i])

    # concatenate the result
    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            x[k] = arr[i][j]
            k += 1
    return x


def plot(t):
    n = []
    for i in range(1, 31):
        n.append((i*10))
    newArr = []
    narr = []
    for i in range(len(n)):
        arr = n[i]*np.log2(n[i]) / 10**5.6
        arrn = n[i] / 10**5.6
        narr.append(arrn)
        newArr.append(arr)
    plt.plot(n, t, label="Bucket Sort")
    # plt.plot(n, newArr, label="nlogn")
    plt.plot(n, narr, label="n")
    plt.xlabel('No. of inputs')
    plt.ylabel('Total time taken')
    plt.title('Bucket Sort analysis')
    plt.legend()
    plt.show()


# main function
if __name__ == "__main__":
    for i in range(2):
        randarr1 = np.random.random(20)
        print(f"Random generated array : {randarr1}")
        # print(BucketSort(randarr1))
        # sorted = BucketSort(randarr1)
        # print(f"Sorted array : {sorted}")
        print(f"Sorted array : {BucketSort(randarr1)}")

    tval = []
    for i in range(1, 31):
        randarr = np.random.random(i*10)
        n = len(randarr)
        start_time = time.perf_counter()
        BucketSort(randarr)
        timeTaken = (time.perf_counter() - start_time)
        tval.append(timeTaken)
        # print(timeTaken, end=" Nano-seconds\n")
    # print(tval)
    plot(tval)
