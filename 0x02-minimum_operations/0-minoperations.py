#!/usr/bin/python3
'''Minimum number of operations'''


def minOperations(n):
    '''Returns number of operations'''
    if n <= 0:
        return 0
    if not isinstance(n, int):
        return 0

    def dp(operation):
        '''Depth search'''
        for i in range(2, int(operation ** 0.5) + 1):
            if operation % i == 0:
                return i + dp(operation // i)
        return operation

    return dp(n)
