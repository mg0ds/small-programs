import math

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]

def binary_search(sequence, target):
    L = 0
    R = len(sequence) - 1
    while L <= R:
        m = math.floor((L + R)/2)
        if sequence[m] < target:
            L = m + 1
        elif sequence[m] > target:
            R = m - 1
        else:
            return m
    return None

#print(binary_search(PRIMES, 13))
