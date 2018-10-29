#! /usr/local/bin/python

'''
Given a list of numbers and a number N, identify all the
indexes of the list whose numbers sum up to the number, N.
'''
def get_list_indexes_that_match_sum (myList, sum):
    result = []
    n = len(myList)

    for i in range(1, 2**n -1):
        tempSum = 0
        index = []

        for j in range(0, n):
            k = 2**j

            if k & i == k:
                index.append(j)
                tempSum += myList[j]

        if sum == tempSum:
            result.append(tuple(index))

    return result


# Test list 1
print (get_list_indexes_that_match_sum([8, 3, 0, -3, 5, -5], 8))

# outputs the list: [(0,), (0, 2), (0, 1, 3), (0, 1, 2, 3), (1, 4), (1, 2, 4), (0, 4, 5), (0, 2, 4, 5), (0, 1, 3, 4, 5)]
