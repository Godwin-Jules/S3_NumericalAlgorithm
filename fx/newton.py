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

def newton(function_verif, function_derivative, begin_value, precision, max_iteration):
    f = function_verif
    f_der = function_derivative
    x_0 = begin_value
    tol = precision
    n_max = max_iteration
    x = x_0
    nbre_it = 0
    while nbre_it < n_max:
        nbre_it += 1
        if f_der(x) == 0:
            print("Erreur mathématique fatale :(")
            exit()
        x_new = x - f(x) / f_der(x)
        error = abs(x_new - x)
        if error < tol:
            break
        else:
            x = x_new
    
    return f"\nRESULTATS :\n\t[Xn, Xn+1] = [{x}, {x_new}]\n\tX_tilde = {(x + x_new) / 2}\n\tNombre d'itérations : {nbre_it}\nMéthode de Newton terminée !"
