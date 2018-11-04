#! /usr/local/bin/python
''' tested with Python 3.7.0 '''

'''
http://www.techiedelight.com/find-minimum-cost-reach-last-cell-matrix-first-cell/
'''

import sys

def min_cost(matrix, m, n, memo):
    '''
    Given a M x N matrix, where each cell has a cost associated with it,
    find the minimum cost to reach last cell (M-1, N-1) of the matrix from its
    first cell (0, 0). We can only move one unit right or one unit left from any cell.
    '''
    if m == 0 or n == 0:
        return sys.maxsize

    if m == 1 and n == 1:
        return matrix[0][0]
    else:
        if (m, n-1) not in memo.keys():
            memo[(m, n-1)] = min_cost(matrix, m, n - 1, memo)

        if (m-1, n) not in memo.keys():
            memo[(m-1, n)] = min_cost(matrix, m-1, n, memo)


        return min(memo[(m, n-1)], memo[(m-1, n)] + matrix[m-1][n-1])


# Test
matrix = [
        [4, 7, 8, 6, 4],
        [6, 7, 3, 9, 2],
        [3, 8, 1, 2, 4],
        [7, 1, 7, 3, 7],
        [2, 9, 8, 9, 3]
    ]

memo = {}
print(min_cost(matrix, len(matrix), len(matrix[0]), memo))
print(memo)