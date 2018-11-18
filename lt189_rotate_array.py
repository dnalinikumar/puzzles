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
    if n == k:
        return
    elif k > n:
        k = k % n

    for i in range(k):
        temp = l[n-k+i]
        l[i+1:n-k+i+1] = l[i:n-k+i]
        l[i] = temp

if __name__ == '__main__':

    lst = [1,2,3,4,5,6,7]
    rotate_array(lst, 3)
    print (lst)

    lst = [-1,-100,3,99]
    rotate_array(lst, 2)
    print (lst)

    lst = [1]
    rotate_array(lst, 1)
    print (lst)

    lst = [1, 2]
    rotate_array(lst, 3)
    print (lst)
