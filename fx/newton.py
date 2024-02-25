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

# def newton(function_verif, function_derivative, born_left, precision, max_iteration):
#     f = function_verif
#     f_der = function_derivative
#     x = born_left
#     tol = precision
#     n_max = max_iteration
#     nbre_it = 0

#     while nbre_it < n_max:
#         nbre_it += 1
#         if f_der(x) == 0:
#             print("Erreur mathématique fatale :(")
#             return "Pas de convergence"
#         x_new = x - f(x) / f_der(x)
#         error = abs(x_new - x)
#         if error < tol:
#             break
#         else:
#             x = x_new
    
#     return f"\nRESULTATS :\n\t[Xn, Xn+1] = [{x}, {x_new}]\n\tX_tilde = {(x + x_new) / 2}\n\tNombre d'itérations : {nbre_it}\nMéthode de Newton terminée !"

def newton(function_verif, function_derivative, born_left, precision, max_iteration):
    f = function_verif
    fprime = function_derivative
    x1 = born_left
    x = 0
    p = precision
    N = max_iteration
    nbre_it = 0
    info_convergence = 0

    while abs(f(x1)) > p and nbre_it < N:
        x = x1
        nbre_it += 1
        if fprime(x) < 1e-15:
            return f"\nRESULTATS :\n\tDérivé quasi null\n\tPas de convergence après {nbre_it} itérations\n\tMéthode de Newton terminée"
        x1 = x - f(x) / fprime(x)
        if abs(f(x1)) <= p:
            info_convergence += 1
            print("Convergence OK")
            break
    if nbre_it == N and info_convergence == 0:
        return f"\nRESULTATS :\n\tNombre maximal d'itérations atteint\n\tPas de convergence après{nbre_it} itérations\nMéthode de Newton terminée"
    elif info_convergence == 1:
        return f"\nRESULTATS :\n\t[a,b] = [{x}, {x1}]\n\tX_tilde = {(x+x1)/2}\n\tNombre d'itérations : {nbre_it}\nMéthode de Newton terminée"
