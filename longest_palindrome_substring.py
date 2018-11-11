#! /usr/local/bin/python
''' tested with Python 3.7.0 '''

def longest_palindrome_substring(s):
    ''' brute force algorithm'''
    n = len(s)
    max_len = 1
    palindrome = []

    for j in range (n, 1, -1):
        for i in range(n - j):
            x = s[i: i+j+1]

            print((f'x={x}'))
            xLen = len(x)

            for k in range(xLen//2):
                if (x[k] != x[xLen-1-k]):
                    break
            else:
                if len(x) >= max_len:
                    max_len = len(x)
                    palindrome.append(x)

    return max_len, palindrome

s = "pttwekewxyqyx"
print(longest_palindrome_substring(s))
