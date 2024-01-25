"""
    Author : Jules Dieu donné
    Date : Tuesday, December 12, 2023
    Motif : equation solving by Dichotomy (Bissection) method
    Inputs :    - the function to verify
                - the limits of the interval [a, b]
                - the precision p (tolerance)
                - the maximum number of iteration

    Outputs :   * the solution interval [a, b]
                * the x tilde value
                * number of iterations
"""

import math

def substitution(f, x_0, tol, n_max):
    x = x_0
    nbre_it = 0
    while nbre_it < n_max:
        nbre_it += 1
        x_new = f(x)
        error = abs(x_new - x)
        if error < tol:
            break
        else:
            x = x_new
    if nbre_it == n_max and abs(x_new - x)  >= tol:
        print("\nLa méthode de substitution n'a pas converge après {} itérations.".format(n_max))
    
    return f"\nRESULTATS :\n\tXn = {x}\n\tXn+1 = {x_new}\n\tNombre d'itérations : {nbre_it}\nMéthode de Substitution terminée !"

# # Exemple d'utilisation
# def f(x):
#     return x**3 - 2*x + x

# result_fixe = substitution(f, -1, 1e-5, 1000000)
# print(result_fixe)

# x_0 = 1.5
# tol = 1e-8
# n_max = 10000000
# x = substitution(f, x_0, tol, n_max)
# print("La solution de l'équation est : ", x)
