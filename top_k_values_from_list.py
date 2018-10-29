#! /usr/local/bin/python

'''
Given a list of numbers, find top k maximum values.
Return the input list if the list has smaller number of elements.
'''
def top_k_max_values_in_a_list(myList, k):

    if (k > len(myList)):
        return myList

    # copy first items of source to target
    top_k_max_list = myList[0:k]

    # check for the rest of the elements
    for i in myList[k:]:
        index, value = min(enumerate(top_k_max_list), key=lambda x: x[1])

        if (i > value):
            top_k_max_list[index] = i

    return top_k_max_list


# Test
print (top_k_max_values_in_a_list([3, 0, -3, 5, -5, 23, 2455, 2, 99, 1020, -222, 8], 5))

# outputs the list: [1020, 99, 2455, 8, 23]