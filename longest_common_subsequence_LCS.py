#! /usr/local/bin/python
''' tested with Python 3.7.0 '''

'''
Given two strings, find the length of the longest common subsequence
Example: X = "ABCBDAB", Y="BDCABA"
it should return 4.
'''
def LCS(X, Y, lenX, lenY):

    # return if we have reached the end of either sequence
    if lenX == 0 or lenY == 0:
        return 0

    # if last character of X and Y matches
    if X[lenX-1] == Y[lenY-1]:
        return 1 + LCS(X, Y, lenX-1, lenY-1)
    else:
        return max(LCS(X, Y, lenX-1, lenY), LCS(X, Y, lenX, lenY-1))





'''
Given two strings, find a longest common subsequence
Example: X = "ABCBDAB", Y="BDCABA"
"BCBA", "BCAB", "BDAB" are longest sequences.
'''
def LCS_string(X, Y, lenX, lenY):

    # return if we have reached the end of either sequence
    if lenX == 0 or lenY == 0:
        return ''

    # if last character of X and Y matches
    if X[lenX-1] == Y[lenY-1]:
        return LCS_string(X, Y, lenX-1, lenY-1) + X[lenX-1]
    else:
        return max(LCS_string(X, Y, lenX-1, lenY), LCS_string(X, Y, lenX, lenY-1))



# Test the results

x = 'ABCBDAB'
y = 'BDCABA'
res = LCS(x, y, len(x), len(y))
print(res)


res = LCS_string(x, y, len(x), len(y))
print(res)


