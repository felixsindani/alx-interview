#!/usr/bin/python3
"""
in-place algorithm to rotate an n x n 2D matrix by 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """
    Rotate 2D Matrix clockwise
    Args:
        matrix (list): 2D square matrix
    Return:
        None
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    for i in range(n):
        for j in range(int(n / 2)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][n-1-j]
            matrix[i][n-1-j] = temp
