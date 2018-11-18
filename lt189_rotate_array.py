#! /usr/local/bin/python
''' tested with Python 3.7.0 '''

'''
Leet code 189:
Given an array, rotate the array to the right by k steps, where k 
is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
'''

def rotate_array(l, k):
    n = len(l)
    if n <= k:
        return l
    elif k > n:
        k = k%n + 1

    for i in range(k):
        temp = l[n-k+i]
        l[i+1:n-k+i+1] = l[i:n-k+i]
        l[i] = temp
    return l


if __name__ == '__main__':
    print(rotate_array([1,2,3,4,5,6,7], 3))

    print(rotate_array([-1,-100,3,99], 2))

    print(rotate_array([1], 1))

    print(rotate_array([1, 2], 3))  # fails in this case. need to check

