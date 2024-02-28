"""
    Author : Jules Dieu donné
    Date : Sunday, February 25, 2024
    Motif : 
    Inputs :    -

    Outputs :   *
"""

import numpy as np
from scipy.linalg import cholesky, cho_factor, cho_solve

def cholevsky(matrice, vector):
    A = np.array(matrice, float)
    b = np.array(vector, float)
    # m_triangle = cholesky(A, lower=True)
    # print(f"La matrice triangulaire de Cholevsky est :\n{m_triangle}")
    Cho, piv = cho_factor(A)
    x = cho_solve(cho_factor(A), b)
    return f"\nLa solution est :\n{x}\n"

# A = np.array([[4, -1, 1],
#               [-1, 5, 3],
#               [1, 3, 5]])
# b = np.array([7, 3, 8])

# r = cholevsky(A, b)
# print(r)