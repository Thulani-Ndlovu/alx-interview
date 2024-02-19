#!/usr/bin/python3
'''Rotate 2D Matrix'''


def rotate_2d_matrix(matrix):
    '''Rotate 2D Matrix 90 degrees'''
    if not isinstance(matrix, list) or not matrix or not all(isinstance(row, list) for row in matrix):
        return

    rows, cols = len(matrix), len(matrix[0])

    if not all(len(row) == cols for row in matrix):
        return

    rotated_matrix = [[0] * rows for _ in range(cols)]

    for r in range(rows):
        for c in range(cols):
            rotated_matrix[c][rows - 1 - r] = matrix[r][c]

    matrix[:] = rotated_matrix
