#! /usr/local/bin/python
''' tested with Python 3.7.0 '''

def LIS(A):
    # validate input
    if type(A) != list:
        return ValueError

    # validate each entry
    for i in A:
        if type(i) != float and type(i) != int:
            return ValueError

    # initialize maximum length for each element as 1.
    L = [1] * len(A)

    for i in range(len(A)):
        for j in range(i):
            if A[j] < A[i] and L[i] < 1 + L[j]:
                L[i] = 1 + L[j]

    return max(L)


A = [5, 7, 4, -3, 9, 1, 10, 4, 5, 8, 9, 3]

print(LIS(A))

