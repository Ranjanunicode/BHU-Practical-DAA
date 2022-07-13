
# 4.  Write a program to implement a priority queue (using Max_Heap). The program should contain the following functions:
# a.	Maximum(S)
# b.	Extract_Max(S)
# c.	Increase_key(S, i, key)
# d.	Insert (A, key)
# Show that each of the above methods takes logn time for running, where n is the problem size.

import matplotlib.pyplot as plt
import numpy as np
import time , random

#Heapify
def Heapify(lst,i,lst_len2):
    left_child = 2 * i + 1  #leftChild child
    right_child = 2 * i + 2 #rightChild child
    if left_child < lst_len2 and lst[left_child] > lst[i]:
        largest = left_child
    else:
        largest = i
    if right_child < lst_len2 and lst[right_child] >=lst[largest]:
        largest = right_child
    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        Heapify(lst, largest,lst_len2)

#Build heap
def BuildHeap(lst):
    for i in range(int((len(lst)/2)-1), -1, -1):
        Heapify(lst,i,len(lst))

#finding Maximum Element
def FindingMax(arr):
    return arr[0]

#Extracting max element
def extractMax2(lst):
    len_lst=len(lst)
    if len_lst<1:
        return -1
    elif lst_len2==1:
        return lst[0]
    else:
        max_element=lst[0]
        lst[0]=lst[len(lst)-1]
        lst=np.delete(lst,len(lst)-1)
        Heapify(lst,0,len(lst))
        return max_element

#Incerase Key
def increaseKey(lst,idx,key):
    if lst[idx]>key:
        return -1
    lst[idx]=key
    while (idx>0 and lst[(idx)//2]<lst[idx]):
        lst[idx],lst[(idx)//2]=lst[(idx)//2],lst[idx]
        idx=idx//2

#Insert A value
def insert(lst,key):
    lst=np.insert(lst,-1,len(lst)+1)
    increaseKey(lst,len(lst)-1,key)
    

#main function
if __name__ == "__main__":
    time_extract_max=[]
    time_increase_key=[]
    time_insert_key=[]
    time_finding_max=[]
    lst_len2=[]
    for i in range(1,50):
        lst=np.random.randint(1,200,i*50)
        lst_len2.append(len(lst))
        BuildHeap(lst)

        st_timer4=time.perf_counter()
        largest=FindingMax(lst)
        time_finding_max.append((time.perf_counter()-st_timer4))
        
        st_timer=time.perf_counter()
        extractMax2(lst)
        time_extract_max.append(((time.perf_counter()-st_timer)))
        
        st_timer1=time.perf_counter()
        increaseKey(lst,random.randint(10,20),random.randint(40,50))
        time_increase_key.append((time.perf_counter()-st_timer1))

        st_timer2=time.perf_counter()
        insert(lst,random.randint(40,60))
        time_insert_key.append((time.perf_counter()-st_timer2))

    logn=[(np.log2(i))/10**4.6 for i in lst_len2] #logn

    # print(lst_len2)
    # print(logn)
    plt.plot(lst_len2,logn,label="logn")
    plt.plot(lst_len2,time_extract_max,label="Extract Max")
    plt.scatter(lst_len2,time_extract_max)
    plt.plot(lst_len2,time_increase_key,label="Increase Key")
    plt.scatter(lst_len2,time_increase_key)
    plt.plot(lst_len2,time_insert_key,label="Insert Key")
    plt.scatter(lst_len2,time_insert_key)
    plt.plot(lst_len2,time_finding_max,label="Finding max")
    plt.scatter(lst_len2,time_finding_max)

    plt.title("All heap operations")
    plt.xlabel("length of lists(n)")
    plt.ylabel("Time")
    
    plt.legend()
    plt.show()
