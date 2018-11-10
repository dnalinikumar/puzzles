#! /usr/local/bin/python
''' tested with Python 3.7.0 '''

def longest_substring_without_repeat_chars(s):
    try_longest = ''
    max_len = 0

    for i in s:
        if i not in try_longest:
            try_longest += i
        else:
            if len(try_longest) > max_len:
                max_len = len(try_longest)
                longest = try_longest
            try_longest = i

    if len(try_longest) > max_len:
        max_len = len(try_longest)
        longest = try_longest

    return max_len, longest


s = "abcdefabcdghijklmnopqera"
print(longest_substring_without_repeat_chars(s))
