import os
import sys

def staircase(n):
    for i in range(n):
        a = []
        for j in range(n-i-1):
          a.append(" ")
        for k in range(i+1):
            a.append("#")
        print("".join(str(x) for x in a))

if __name__ == '__main__':
    n = int(input())

    staircase(n)
