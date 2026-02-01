#!/usr/bin/env python3
matrix = [[1, 3, 9, 4, 5, 8], [2, 4, 7, 3, 4, 0], [0, 3, 4, 6, 1, 5]]
the_middle = []
for i in range(len(matrix)):
    the_middle.append([matrix[i][len(matrix[0]) // 2 - 1], matrix[i][len(matrix[0]) // 2]])
print("The middle rows of the matrix are: {}".format(the_middle))
