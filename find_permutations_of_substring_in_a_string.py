#! /usr/local/bin/python
''' tested with Python 3.7.0 '''

'''
Given a string X and another small string y, identify all the 
permutations of y in X. Return the substrings in a list. 
'''

''' Get the map of characters for a given string'''
def get_dict_of_string(z):
    z_dict = {}
    for i in z:
        if i in z_dict.keys():
            z_dict[i] += 1
        else:
            z_dict[i] = 1

    return z_dict


''' do the actual compute.'''
def find_permutations_of_substring_in_a_string(longStr, shortStr):
    # Assuming valid inputs are given for x, y; len(x) > len(y)

    result = []

    # Get the map of the substring
    y_dict = get_dict_of_string(shortStr)

    for i in range(len(longStr)):
        tempString = longStr[i: i + len(shortStr)]
        x_dict_n = get_dict_of_string(tempString)

        if x_dict_n == y_dict:
            result.append(tempString)

    return result


res = find_permutations_of_substring_in_a_string("abcdefghsdfasdfaldjflajsdjflkadsjflasdjjfdf", "asdjj")
print(res)





