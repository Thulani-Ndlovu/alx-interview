#!/usr/bin/python3
'''Pascal Triangle function'''


def pascal_triangle(n):
    """Generates the nth row of Pascal's triangle."""
    pascalTriangle = []

    if n <= 0:
        return pascalTriangle

    for i in range(n):
        pascalTriangle.append([])
        for j in range(i + 1):
            if j == 0 or j == i:
                pascalTriangle[i].append(1)
            else:
                pascalTriangle[i].append(pascalTriangle[i - 1][j - 1] +
                                         pascalTriangle[i - 1][j])

    return pascalTriangle
