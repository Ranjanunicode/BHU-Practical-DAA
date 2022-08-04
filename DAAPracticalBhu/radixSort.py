# 7. Write a program to implement Radix Sort algorithm.
# Also plot the graph of the time complexity for different values of array size ‘n’.

## Radix Sort ########################

import time
import numpy as np
import matplotlib.pyplot as plt


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


def plot(t):
    nsq = []
    n = []
    for i in range(1, 31):
        n.append((i*100))
    newArr = []
    narr = []
    for i in range(len(n)):
        arr = n[i]*np.log2(n[i]) / 10**8
        arrn = n[i] / 10**5
        narr.append(arrn)
        newArr.append(arr)

    plt.plot(n, t, label="Radix Sort")
    # plt.plot(n, newArr, label="nlogn")
    plt.plot(n, narr, label="n")
    plt.xlabel('No. of inputs')
    plt.ylabel('Total time taken')
    plt.title('Radix Sort analysis')
    plt.legend()
    plt.show()


# main function
if __name__ == "__main__":
    for i in range(2):
        randarr1 = np.random.randint(1, 200, 20)
        print(f"Random generated array : {randarr1}")
        radixSort(randarr1)
        sorted = randarr1
        print(f"Sorted array : {sorted}")

    tval = []
    for i in range(1, 31):
        randarr = np.random.randint(1, 200, i*100)
        n = len(randarr)
        start_time = time.perf_counter()
        radixSort(randarr)
        timeTaken = (time.perf_counter() - start_time)
        tval.append(timeTaken)
    plot(tval)
