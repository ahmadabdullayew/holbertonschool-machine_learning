#!/usr/bin/env python3
def matrix_transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    new_matrix = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            new_matrix[j][i] = matrix[i][j]

    return new_matrix