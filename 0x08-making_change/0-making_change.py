#!/usr/bin/python3
'''Making Change'''


def makeChange(coins, total):
    '''make change function'''
    if total <= 0:
        return 0
    remainder = total
    coinsCount = 0
    coinIndex = 0
    sortedCoins = sorted(coins, reverse=True)
    numCoins = len(coins)
    while remainder > 0:
        if coinIndex >= numCoins:
            return -1
        if remainder - sortedCoins[coinIndex] >= 0:
            remainder -= sortedCoins[coinIndex]
            coinsCount += 1
        else:
            coinIndex += 1
    return coinsCount
