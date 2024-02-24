"""
    Author : Jules Dieu donné
    Date : Tuesday, December 12, 2023
    Motif : equation solving by Dichotomy (Bissection) method
    Inputs :    - the function to verify
                - the limits of the interval [a, b]
                - the precision p (tolerance)

    Outputs :   * verification of the convergence
                * the solution interval [a, b]
                * the x tilde value
                * number of iterations
"""

import math

def corde(f,x0,x1,p,N):
    nbre_it = 0
    if f(x1) == 0 or f(x0) == 0 or f(x1) - f(x0) == 0:
        print("Erreur mathématique : division par zéro :(")
        return "Pas de convergence"
    else:
        xn = x1 - ((f(x1)*(x1 - x0)) / (f(x1) - f(x0)))
    while nbre_it < N:
        nbre_it += 1
        if abs(xn - x1) < p:
            print("\nConvergence OK !")
            break
        else:
            x0 = x1
            x1 = xn
            if f(x1) == 0 or f(x0) == 0 or f(x1) - f(x0) == 0:
                print("Pas de convergeance")
                break
            else:
                xn = x1 - ((f(x1)*(x1 - x0)) / (f(x1) - f(x0)))
    if nbre_it == N:
        print(f"\nPas de convergence avec cette méthode après {nbre_it} itérations !")
    
    return f"\nRESULTATS :\n\t[Xn-1, Xn] = [{x0}, {x1}]\n\tXn+1 = {x1 - ((f(x1)*(x1 - x0)) / (f(x1) - f(x0)))}\n\tNombre d'itérations : {nbre_it}"