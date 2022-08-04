# Write a program to perform integer integer multiplication using Divide and Conquer technique.
# compare n^2 and n^1.6

import math
import time
import random
import matplotlib.pyplot as plt

MAXSIZE = 50000
STEPS = 6000


def multiply(x, y):
    # Convert x into it's binary form
    xb = bin(x)
    xb = xb[2:]
    # Convert y into it's binary form
    yb = bin(y)
    yb = yb[2:]

    len_y = len(yb)
    len_x = len(xb)

    if x > y:
        n = len(xb)
        while(len_y < len_x):
            yb = '0' + yb
            len_y = len_y + 1

    else:
        n = len(yb)
        while(len_x < len_y):
            xb = '0' + xb
            len_x = len_x + 1

    # Base Condition
    if n == 1:
        return x * y

    len_xL = len_x//2
    len_yL = len_y//2

    xL = xb[:len_xL]
    xR = xb[len_xL:]
    yL = yb[:len_yL]
    yR = yb[len_yL:]

    # Multiply xL and yL
    mul = int(xL, 2) * int(yL, 2)
    P1 = bin(mul)
    P1 = P1[2:]

    # Multiply xR and yR
    mul = int(xR, 2) * int(yR, 2)
    P2 = bin(mul)
    P2 = P2[2:]

    # Multiply xL+xR and yL+yR
    add1 = int(xL, 2) + int(xR, 2)
    add2 = int(yL, 2) + int(yR, 2)
    mul = add1 * add2
    P3 = bin(mul)
    P3 = P3[2:]

    mul = int(P1, 2) * 2*(2*math.ceil(n/2)) + (int(P3, 2) -
                                               int(P1, 2) - int(P2, 2)) * 2*(math.ceil(n/2)) + int(P2, 2)
    return mul


if __name__ == '__main__':
    n = []
    et = []
    n16_x = []
    n16_y = []
    n15_x = []
    n15_y = []
    for i in range(0, MAXSIZE+1, STEPS):
        x = random.randint(i, 10**i)
        y = random.randint(i, 10**i)
        start = time.perf_counter_ns()
        z = multiply(x, y)
        end = time.perf_counter_ns()
        n.append(len(str(x)))
        executionTime = (end - start)*1.5
        et.append(executionTime)
        n16_x.append(len(str(x)))
        n16_y.append(i**(1.6))
        n15_x.append(len(str(x)))
        n15_y.append(i**(1.5))
    print(n)
    print(et)
    print(n16_y)

    plt.plot(n, et, label="mul")
    plt.plot(n16_x, n16_y, label="n^1.6")
    plt.plot(n15_x, n15_y, label="n^1.5")
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('integer multiplication')
    plt.legend()
    plt.show()
