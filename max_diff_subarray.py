#! /usr/local/bin/python
''' tested with Python 3.7.0 '''

'''
  Problem: 
      Given an array of numbers, find the maximum difference possible when the array is split into two subarrays. 

 Solution: 
   For a given array, the maximum sum can be achieved as follows.
   1. If there are negative numbers, all positive numbers are in one set, and all negative numbers are in second set. 
   2. If there are only positive numbers, the minimum positive number is made into second set. 
'''

def max_diff_subarrays(lst):
    max_diff = float('-inf')
    negative_sum = 0 
    positive_sum = 0 
    minimum_positive_number = float('inf')

    for i in range(len(lst)): 
        # If there are negative numbers, get the negative sum. 
        if lst[i] < 0:
            negative_sum += lst[i]
        else:
            positive_sum += lst[i]
            if lst[i] < minimum_positive_number:
                minimum_positive_number = lst[i]
 
    if negative_sum < 0:
        return positive_sum - negative_sum
    else:
        return positive_sum - minimum_positive_number

if __name__ == '__main__':
    x = [15, 8, 9, 10, 27, 3, -3]
    print ("maximum difference:", max_diff_subarrays(x))

