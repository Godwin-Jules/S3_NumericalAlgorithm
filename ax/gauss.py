"""
    Author : Jules Dieu donné
    Date : Thursday, January 24, 2024
    Motif : 
    Inputs :    -

    Outputs :   *
"""

import numpy as np

def gauss(A, b):
    n = A.shape[0]  # nb de lignes
    m = A.shape[1]  # nb de colonnes
    M = np.zeros([n, m+1])  # matrice de travail : matrice augmentée de Ab
    M[:,0:m] = A
    M[:,m] = b
    sol = np.zeros(n)
    # Echelonnement
    for i in np.arange(0, n-1): #boucle en i (pivots) de 1 à n-1 // 0, 1, 2, ..., n-2
        for k in np.arange(i+1):    #boucle de k (lignes) de i+1 à n / i+1, i+2, ..., n-1
            M[k,:] = A[k,:] - M[k,i] / M[i,i] * M[i,:]
    # Remontée
    