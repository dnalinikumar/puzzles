#! /usr/local/bin/python
''' tested with Python 3.7.0 '''

def longest_substring_without_repeat_chars(s):
    longest = ''
    max_len = 0

    for i in s:
        if i not in longest:
            longest += i
        else:
            if len(longest) > max_len:
                max_len = len(longest)
            longest = i

    if len(longest) > max_len:
        max_len = len(longest)

    return max_len


s = "abcdefabcdghijklmnopqera"
print(longest_substring_without_repeat_chars(s))
