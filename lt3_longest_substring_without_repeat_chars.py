#! /usr/local/bin/python
''' tested with Python 3.7.0 '''

'''
Leet Code 3
Given a string, find the length of the longest substring without 
repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is 
             a subsequence and not a substring
'''

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
