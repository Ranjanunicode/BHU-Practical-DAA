# 3.  Write a program to perform heapsort on an n-length array. 
# You should first construct the heap from the array and then perform heapsort and print the correct 
# sorted sequence of the input array. 
# Also analyze the time complexity of the algorithm by plotting the graph of running time 
# of the algorithm for different values of n and comparing it with nlogn. Give your comments.

def heapify(arr, n, i):
    largest = i  
    l = 2 * i + 1
    r = 2 * i + 2	

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

def plot(t):
    nsq = []
    n = []
    for i in range(1, 31):
        n.append((i*1000))
    # n = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, ...]
    newArr = []
    for i in range(len(n)):
        arr = n[i]*np.log2(i) / 10**5.2
        newArr.append(arr)


    plt.plot(n, t, label="heap sort")
    plt.plot(n, newArr, label="nlogn")
    plt.xlabel('No. of inputs')
    plt.ylabel('Total time taken')
    plt.title('Merge Sort analysis')
    plt.legend()
    plt.show()

# main function
if __name__=="__main__":
    tval = []
    for i in range(1, 31):
        randarr = np.random.randint(1, 200, i*1000)
        n = len(randarr)
        start_time = time.perf_counter()
        heapSort(randarr)
        timeTaken = (time.perf_counter() - start_time)
        tval.append(timeTaken)
        # print(timeTaken, end=" Nano-seconds\n")
    print(tval)
    plot(tval)
