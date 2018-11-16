#! /usr/local/bin/python
''' tested with Python 3.7.0 '''

'''
Find the median of the two sorted numbered arrays (x, y) with sizes m & n respectively.
Time complexity is O(log(m+n)). 
'''
def find_median_of_sorted_arrays_of_diff_sizes(x, y):
    m, n, = len(x), len(y)
    total_len = m + n
    is_even =  total_len % 2 == 0
    half_len = (total_len + 1)//2

    # we need m to be smaller than n
    if m > n:
        m, n, x, y = n, m, y, x

    if m == 0:
        raise ValueError

    low, high = 0, m

    while low <= high:
        xPartition = (low + high)//2
        yPartition = half_len - xPartition

        if xPartition == 0:
            maxLeftX = float('-inf')
        else:
            maxLeftX = x[xPartition - 1]

        if xPartition == m:
            minRightX = float('inf')
        else:
            minRightX = x[xPartition]

        if yPartition == 0:
            maxLeftY = float('-inf')
        else:
            maxLeftY = y[yPartition -1]

        if yPartition == n:
            minRightY = float('inf')
        else:
            minRightY = y[yPartition]

        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            if is_even:
                return (max(maxLeftY, minRightX) + min(maxLeftX, minRightY))/2
            else:
                return max(maxLeftX, maxLeftY)
        elif maxLeftX > minRightY:
            high = xPartition - 1
        else:
            low = xPartition + 1

    raise ValueError

if __name__ == "__main__":
    x = [1, 3, 8, 9, 15]
    y = [7, 11, 19, 21, 24, 25]
    print(find_median_of_sorted_arrays_of_diff_sizes(x, y))

    x = [1]
    y = [3, 8, 7, 9, 11, 15, 19, 21, 24, 25]
    print(find_median_of_sorted_arrays_of_diff_sizes(x, y))

    x = [1, 19, 21, 24, 25]
    y = [3, 8, 7, 9, 11, 15]
    print(find_median_of_sorted_arrays_of_diff_sizes(x, y))

