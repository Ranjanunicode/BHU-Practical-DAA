# 2. Write a program to perform Integer Multiplication using Divide and Conquer technique.
# Plot the graph showing time taken for running the program for different sizes of input integer numbers.
# Compare the curve with the curve of n^2 and n^1.6 and give your comments.


import time
import matplotlib.pyplot as plt
import random
# global variable
MAXSIZE = 2000
STEPS = 200

# Function to make the binary strings of equal length
def makeequallength(xb, yb):
    len_x = len(xb)
    len_y = len(yb)
    if len(xb) > len(yb):
        n = len(xb)
        while(len_y < len_x):
            yb = '0' + yb
            len_y = len_y + 1

    else:
        n = len(yb)
        while(len_x < len_y):
            xb = '0' + xb
            len_x = len_x + 1

    return (n, xb, yb, len_x, len_y)

# Function to add two binary numbers
def add(x, y):
    x = int(x, 2)
    y = int(y, 2)
    sum = bin(x + y)
    sum = sum[2:]
    return sum
# Function to multiply two integers using divide and conquer
def multiply(xb, yb):
    (n, xb, yb, len_x, len_y) = makeequallength(xb, yb)

    # Base Condition
    if n == 0:
        return 0

    # Multiply two single bit binary numbers
    if n == 1:
        return int(xb, 2) * int(yb, 2)

    fh = n//2
    sh = n - fh

    xL = xb[:fh] 
    xR = xb[fh:]  
    yL = yb[:fh] 
    yR = yb[fh:]  

    add1 = add(xL, xR)
    add2 = add(yL, yR)

    P1 = multiply(xL, yL)
    P2 = multiply(xR, yR)
    P3 = multiply(add1, add2)

    return P1*(1 << (2*sh)) + (P3 - P1 - P2)*(1 << sh) + P2


def plot(n, t):
    nsq = []
    n16 = []
    n159 = []
    n15 = []
    for i in range(len(n)):
        # nsq.append((n[i]*n[i])*1000*5)
        n16.append((n[i]**1.6)/ (10**5))
        n15.append((n[i]**1.5)/ (10**5))
        n159.append((n[i]**1.59)/ (10**5))

    # plt.plot(n, nsq, label="n^2")
    plt.plot(n, t, label="int mul")
    plt.plot(n, n16, label="n^1.6")
    plt.plot(n, n15, label="n^1.5")
    plt.plot(n, n159, label="n^1.59")
    plt.xlabel('No. of inputs')
    plt.ylabel('Total time taken')
    plt.title('Integer Multiplication analysis')
    plt.legend()
    plt.show()

# main function
if __name__ == '__main__':

    tval = []
    nval = []

    for i in range(0, MAXSIZE+1, STEPS):
        x = random.randint(i, 10**i)
        y = random.randint(i, 10**i)
        xb = bin(x)
        xb = xb[2:] 
        yb = bin(y)
        yb = yb[2:] 
        mlen = max(len(xb), len(yb))
        nval.append(mlen)
        start = time.perf_counter()
        result = multiply(xb, yb)
        end = time.perf_counter()
        pt = (end - start)
        tval.append(pt)
        # print(pt)
    plot(nval, tval)
