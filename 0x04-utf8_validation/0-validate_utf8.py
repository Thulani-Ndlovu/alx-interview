#!/usr/bin/python3
'''UTF-8 Validation'''


def validUTF8(data):
    '''determines if a given data set represents a valid UTF-8 encoding'''
    length = len(data)
    next = 0

    for idx in range(length):
        if next > 0:
            next -= 1
            continue
        if type(data[idx]) != int or data[idx] < 0 or data[idx] > 0x10ffff:
            return False
        elif data[idx] <= 0x7f:
            next = 0
        elif data[idx] & 0b11111000 == 0b11110000:
            span = 4
            if length - idx >= span:
                nextBody = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[idx + 1: idx + span],
                ))
                if not all(nextBody):
                    return False
                next = span - 1
            else:
                return False
        elif data[idx] & 0b11110000 == 0b11100000:
            span = 3
            if length - idx >= span:
                nextBody = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[idx + 1: idx + span],
                ))
                if not all(nextBody):
                    return False
                next = span - 1
            else:
                return False
        elif data[idx] & 0b11100000 == 0b11000000:
            span = 2
            if length - idx >= span:
                nextBody = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[idx + 1: idx + span],
                ))
                if not all(nextBody):
                    return False
                next = span - 1
            else:
                return False
        else:
            return False
    return True
