# Факториал.

import sys


def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

line = sys.stdin.readline()
print(factorial(int(line)))
