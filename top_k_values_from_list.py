#! /usr/local/bin/python
''' tested with Python 3.7.0 '''

'''
Given a list of numbers, find top k maximum values.
Return the input list if the list has smaller number of elements.
'''
def top_k_max_values_in_a_list(myList, k):
    
    # Not added checks here to validate myList and k.

    if k > len(myList):
        return myList

    # copy first items of source to target
    top_k_max_list = myList[0:k]

    # check for the rest of the elements
    for i in myList[k:]:
        value = min(top_k_max_list)

        if i > value:
            index = top_k_max_list.index(value)
            top_k_max_list[index] = i

    return top_k_max_list


if __name__ == '__main__':
    # Test
    print (top_k_max_values_in_a_list([3, 0, -3, 5, -5, 23, 2455, 2, 99, 1020, -222, 8], 5))

    # outputs the list: [1020, 99, 2455, 8, 23]
