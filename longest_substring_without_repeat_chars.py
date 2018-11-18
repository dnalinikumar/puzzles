#! /usr/local/bin/python
''' tested with Python 3.7.0 '''

def longest_substring_without_repeat_chars(s):
    try_longest = ''
    max_len = 0

    for i in s:
        if i not in try_longest:
            try_longest += i
        else:
            index = try_longest.index(i)
            try_longest = try_longest[index+1:] + i

        if (len(try_longest) > max_len):
            max_len = len(try_longest)
            longest = try_longest

    return max_len, longest


if __name__ == '__main__'
    s = "abcdefabcdghijklmnopqera"
    print(longest_substring_without_repeat_chars(s))
