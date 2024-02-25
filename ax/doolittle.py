"""
    Author : Jules Dieu donné
    Date : Sunday, February 25, 2024
    Motif : 
    Inputs :    -

    Outputs :   *
"""

import numpy as np
from scipy.linalg import lu, lu_factor, lu_solve

def doolittle(matrice, vector):
    A = matrice
    b = vector
    p, L, U = lu(A)
    print(f"\nLa matrice L est :\n{L}")
    print(f"\nLa matrice U est :\n{U}")
    LU, piv = lu_factor(A)
    x = lu_solve((LU, piv), b)
    return f"\n\nLa solution est :\n{x}\n"