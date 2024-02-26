"""
    Author : Jules Dieu donné
    Date : Sunday, February 25, 2024
    Motif : 
    Inputs :    -

    Outputs :   *
"""

import numpy as np

def diag_dominante(matrix):
    n = len(matrix)

    for i in range(n):
        diagonal_element = abs(matrix[i, i])
        row_sum = np.sum(np.abs(matrix[i, :])) - diagonal_element
        if diagonal_element <= row_sum:
            return False

    return True