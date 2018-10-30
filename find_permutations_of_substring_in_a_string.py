#! /usr/local/bin/python
''' tested with Python 3.7.0 '''

'''
Given a string X and another small string y, identify all the 
permutations of y in X. Return the substrings in a list. 
'''

''' Get the map of characters for a given string'''
def get_dict_of_string(z):
    zDict = {}
    for i in z:
        if i in zDict.keys():
            zDict[i] += 1
        else:
            zDict[i] = 1

    return zDict


''' do the actual compute.'''


def find_permutations_of_substring_in_a_string(longStr, shortStr):
    # Assuming valid inputs are given for longStr, shortStr; len(longStr) > len(shortStr)

    result = []
    shortLen = len(shortStr)
    longLen = len(longStr)

    # Get the map of the short string
    shortDict = get_dict_of_string(shortStr)

    # Get the map of long string till substring length
    snippet = longStr[:shortLen]
    snippetDict = get_dict_of_string(snippet)

    if shortDict == snippetDict:
        result.append(snippet)

    # iterate through rest character by character.
    j = 0
    for i in range(shortLen, longLen):

        front = longStr[j]
        rear = longStr[i]

        # add/increment the count for end char in dictionary.
        if rear in snippetDict.keys():
            snippetDict[rear] += 1
        else:
            snippetDict[rear] = 1

        # subtract/delete the count for begin char in dictionary.
        if snippetDict[front] == 1:
            del snippetDict[front]
        else:
            snippetDict[front] -= 1

        # point the front index to next character
        j += 1

        # check if the dictionaries are equal
        if shortDict == snippetDict:
            result.append(longStr[j: j+shortLen])

    return result


res = find_permutations_of_substring_in_a_string("abcdefghsdfasdfaldjflajsdjflkadsjflasdjjfdf", "asdjj")
print(res)





