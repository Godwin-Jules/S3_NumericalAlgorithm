"""
    Author : Jules Dieu donné
    Date : Sunday, February 25, 2024
    Motif : 
    Inputs :    -

    Outputs :   *
"""

import numpy as np

def gauss_jordan(A, b):
    a = np.array(A, float)
    b = np.array(b, float)
    n = len(b)

    for k in range(n):
        # partial pivoting
        if np.fabs(a[k,k]) < 1.e-12:
            for i in range(k+1,n):
                if np.fabs(a[i,k]) > np.fabs(a[k,k]):
                    for j in range(k,n):
                        A[k,j], A[i,j] = A[i,j], A[k,j]
                    b[k], b[i] = b[i], b[k]
                    break
        # Division of the pivot row
        pivot = A[k,k]
        for j in range(k,n):
            A[k,j] /= pivot
        b[k] /= pivot
        #Elimination loop
        for i in range(n):
            if i == k or A[i,k] == 0: continue
            factor = A[i,k]
            for j in range(k,n):
                A[i,j] -= factor * A[k,j]
            b[i] -= factor * b[k]
    return f"\n\nLa solution est :\n{b}\n"


# A = np.array([[0, 2, 0, 1],
#      [2, 2, 3, 2],
#      [4, -3, 0, 1],
#      [6, 1, -6, -5]], float)
# b = np.array([0, -2, -7, 6], float)

# x,a = gauss_jordan(A,b)
# print(f"\n\nThe solution is :\n{x}")
# print(f"The transformed A is :\n{a}")
