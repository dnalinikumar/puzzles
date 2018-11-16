#! /usr/local/bin/python
''' tested with Python 3.7.0 '''

def fib_iter(n):
    '''find nth term in fibonacci series'''
    if n < 0:
        raise NotImplementedError

    f = [0, 1]

    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])

    return f[n]


def fib_memo(n, memo):
    '''Finding nth fibonacci term using memoization.'''
    if n < 0:
        raise NotImplementedError
    elif n <= 1:
        memo[n] = n
        return n
    else:
        if not memo[n-1]:
            memo[n - 1] = fib_memo(n-1, memo)

        if not memo[n - 2]:
            memo[n - 2] = fib_memo(n-2, memo)

        return memo[n-1] + memo[n-2]


if __name__ == "__main__":
    # Test
    print (fib_iter(10))

    memo = [None] * 10
    print (fib_memo(10, memo))
