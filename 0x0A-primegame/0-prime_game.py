#!/usr/bin/python3
'''Prime Game'''


def isPrime(num):
    '''Check if num is a prime number'''
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def roundWinner(n):
    '''Determines the winner of a round'''
    primeSet = set()
    for i in range(2, n + 1):
        if isPrime(i):
            primeSet.add(i)

    maria = True
    while primeSet:
        if maria:
            removePrime = min(primeSet)
        else:
            removePrime = max(primeSet)
        primeSet.remove(removePrime)
        for mul in range(removePrime, n + 1, removePrime):
            primeSet.discard(mul)
        maria = not maria

    return "Maria" if not maria else "Ben"


def isWinner(x, nums):
    '''Winner of the Game'''
    maria = 0
    ben = 0

    for num in nums:
        winner = roundWinner(num)
        if winner == "Maria":
            maria += 1
        elif winner == "Ben":
            ben += 1

    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"
    else:
        return None
