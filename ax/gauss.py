"""
    Author : Jules Dieu donné
    Date : Thursday, January 24, 2024
    Motif : 
    Inputs :    -

    Outputs :   *
"""

import numpy as np
from scipy.linalg import solve

def gauss(matrice, vector):
    A = np.array(matrice, float)
    b = np.array(vector, float)
    n = A.shape[0]
    m = A.shape[1]
    M = np.hstack( (A, np.array([b]).T) )
    Aw = np.zeros([n, n+1])
    Aw[:, 0:n] = A
    Aw[:,n] = b
    x = np.zeros(n)
    
    # Echélonnement
    for i in np.arange(0, n-1):
        # Recherche d'un pivot non nul
        if abs(M[i,i]) < 1e-15:
            for k in np.arange(i+1,n):
                if abs(M[k,k]) > 1e-15:
                    pivot_ok = k
                    break
            # Permutation entre la ligne i et la ligne k
            copy_M = np.copy(M[i,:])
            M[i,:] = M[pivot_ok,:]
            M[pivot_ok,:] = copy_M
        #Echélonnement
        for k in np.arange(i+1, n):
            M[k,:] = M[k,:] - M[k,i] / M[i,i] * M[i,:]     # La formule de calul est : A(k, :) = A(k, :) /A(i, i) * A(i, :)
    # print(f"Après échélonnement, la matrice augmentée devient :\n{M}")
    
    # La remontée
    x[n-1] = M[n-1, n] / M[n-1, n-1]
    for i in np.arange(n-2, -1, -1):    # boucle de n-2 à 0 // n-1 à 1
        x[i] = ( M[i, n] - np.sum(M[i, i+1:n] * x[i+1:n]) ) / M[i, i]

    # Vérification avec l'algo de python
    # verif = np.matmul(A, x)     # on doit trouver b
    # solnumpy = solve(A, b)      # on doit trouver x
    return f"\n\tLa solution est :\n{x}\n"
