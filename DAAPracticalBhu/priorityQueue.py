# 4.  Write a program to implement a priority queue (using Max_Heap). The program should contain the following functions:
# a.	Maximum(S)
# b.	Extract_Max(S)
# c.	Increase_key(S, i, key)
# d.	Insert (A, key)

# Show that each of the above methods takes logn time for running, where n is the problem size.

# using array implementation of
# binary heap

import numpy as np

H = [0]*50
size = -1


def parent(i):
    return (i - 1) // 2


def leftChild(i):
    return ((2 * i) + 1)


def rightChild(i):
    return ((2 * i) + 2)


def shiftUp(i):
    while (i > 0 and H[parent(i)] < H[i]):
        swap(parent(i), i)
        # Update i to parent of i
        i = parent(i)


def shiftDown(i):
    maxIndex = i
    # Left Child
    l = leftChild(i)
    if (l <= size and H[l] > H[maxIndex]):
        maxIndex = l
    # Right Child
    r = rightChild(i)
    if (r <= size and H[r] > H[maxIndex]):
        maxIndex = r
    # If i not same as maxIndex
    if (i != maxIndex):
        swap(i, maxIndex)
        shiftDown(maxIndex)


def insert(p):
    global size
    size = size + 1
    H[size] = p
    shiftUp(size)


def extractMax():
    global size
    result = H[0]
    # Replace the value at the root with the last leaf
    H[0] = H[size]
    size = size - 1
    # Shift down the replaced # element to maintain the heap property
    shiftDown(0)
    return result


def changePriority(i, p):
    oldp = H[i]
    H[i] = p
    if (p > oldp):
        shiftUp(i)
    else:
        shiftDown(i)


def getMax():
    return H[0]


def Remove(i):
    H[i] = getMax() + 1
    shiftUp(i)
    # Extract the node
    extractMax()


def swap(i, j):
    temp = H[i]
    H[i] = H[j]
    H[j] = temp


if __name__ == "__main__":
    # Insert the element to the
    # priority queue
    for i in range(10):
        insert(np.random.randint(1, 200))
    # insert(45)
    # insert(70)
    # insert(14)
    # insert(12)
    # insert(3)
    # insert(7)
    # insert(11)
    # insert(23)
    # insert(71)

    i = 0

    # Priority queue before extracting max
    print("Priority Queue : ", end="")
    while (i <= size):

        print(H[i], end=" ")
        i += 1

    print()

    # Node with maximum priority
    print("Node with maximum priority :", extractMax())

    # Priority queue after extracting max
    print("Priority queue after extracting maximum : ", end="")
    j = 0
    while (j <= size):

        print(H[j], end=" ")
        j += 1

    print()

    # Change the priority of element
    # present at index 2 to 49
    changePriority(2, 49)
    print("Priority queue after priority change : ", end="")
    k = 0
    while (k <= size):

        print(H[k], end=" ")
        k += 1

    print()

    # Remove element at index 3
    Remove(3)
    print("Priority queue after removing the element : ", end="")
    l = 0
    while (l <= size):
        print(H[l], end=" ")
        l += 1


# # 4.  Write a program to implement a priority queue (using Max_Heap). The program should contain the following functions:
# # a.	Maximum(S)
# # b.	Extract_Max(S)
# # c.	Increase_key(S, i, key)
# # d.	Insert (A, key)

# # Show that each of the above methods takes logn time for running, where n is the problem size.

# import time
# import numpy as np
# import matplotlib.pyplot as plt

# H = [0]*50
# size = -1


# def parent(i):
#     return (i - 1) // 2


# def leftChild(i):
#     return ((2 * i) + 1)


# def rightChild(i):
#     return ((2 * i) + 2)


# def shiftUp(i):
#     while (i > 0 and H[parent(i)] < H[i]):
#         swap(parent(i), i)
#         # Update i to parent of i
#         i = parent(i)


# def shiftDown(i):
#     maxIndex = i
#     # Left Child
#     l = leftChild(i)
#     if (l <= size and H[l] > H[maxIndex]):
#         maxIndex = l
#     # Right Child
#     r = rightChild(i)
#     if (r <= size and H[r] > H[maxIndex]):
#         maxIndex = r
#     # If i not same as maxIndex
#     if (i != maxIndex):
#         swap(i, maxIndex)
#         shiftDown(maxIndex)


# def insert(p):
#     global size
#     size = size + 1
#     H[size] = p
#     shiftUp(size)


# def extractMax():
#     global size
#     result = H[0]
#     # Replace the value at the root with the last leaf
#     H[0] = H[size]
#     size = size - 1
#     # Shift down the replaced # element to maintain the heap property
#     shiftDown(0)
#     return result


# def changePriority(i, p):
#     oldp = H[i]
#     H[i] = p
#     if (p > oldp):
#         shiftUp(i)
#     else:
#         shiftDown(i)


# def getMax():
#     return H[0]

# # remove the element from the priority queue
# def Remove(i):
#     H[i] = getMax() + 1
#     shiftUp(i)
#     # Extract the node
#     extractMax()

# def swap(i, j):
#     temp = H[i]
#     H[i] = H[j]
#     H[j] = temp

# def plot(t,array):
#     newArr = []
#     for i in range(len(array)):
#         arr = np.log2(array[i])
#         newArr.append(arr)

#     plt.plot(t, newArr, label="logn")
#     plt.xlabel('No. of inputs')
#     plt.ylabel('Total time taken')
#     plt.title('Priority Queue analysis')
#     plt.legend()
#     plt.show()

# if __name__ == "__main__":
#     for i in range(20):
#         num = np.random.randint(1, 200)
#         insert(num)

#     i = 0
#     # Priority queue before extracting max
#     print("Priority Queue : ", end="")
#     while (i <= size):
#         print(H[i], end=" ")
#         i += 1
#     print()

#     # Node with maximum priority
#     print("Node with maximum priority :", extractMax())
#     # Priority queue after extracting max
#     print("Priority queue after extracting maximum : ", end="")
#     j = 0
#     while (j <= size):
#         print(H[j], end=" ")
#         j += 1
#     print()

#     # Change the priority of element
#     # present at index 2 to 199
#     changePriority(2, 199)
#     print("Priority queue after priority change : ", end="")
#     k = 0
#     while (k <= size):
#         print(H[k], end=" ")
#         k += 1
#     print()

#     # Remove element at index 3
#     Remove(3)
#     print("Priority queue after removing the element : ", end="")
#     l = 0
#     while (l <= size):
#         print(H[l], end=" ")
#         l += 1
