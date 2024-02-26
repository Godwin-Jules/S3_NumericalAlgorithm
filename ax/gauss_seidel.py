"""
    Author : Jules Dieu donné
    Date : Sunday, February 25, 2024
    Motif : 
    Inputs :    -

    Outputs :   *
"""

import numpy as np

def gauss_seidel(matrice, vector, begin_matrice, max_iteration):
    A = matrice
    b = vector
    x = begin_matrice
    N = max_iteration
    D = np.diag(np.diag(A))
    E = - np.tril(A,-1)
    F = - np.triu(A,1)
    nbre_it = 0
    while nbre_it < N:
        nbre_it += 1
        x = np.dot(np.linalg.inv(D-E), np.dot(F,x) + b)
    return f"\nAprès {nbre_it} itérations, la solution est :\n{x}\n"

A = np.array([[4,3,3],
              [3,4,3],
              [3,3,4]])
b = np.array([10,10,10])
x = np.array([0,0,0])
print(gauss_seidel(A,b,x,10))