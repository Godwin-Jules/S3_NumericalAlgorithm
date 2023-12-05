"""
    Author : Jules Dieu donné
    Date : unknown
    Motif : equation solving by Dichotomy (Bissection) method
    Inputs :    - the function to verify
                - the limits of the interval [a, b]
                - the precision p (tolerance)

    Outputs :   * the solution interval [a, b]
                * the x tilde value
                * number of iterations
"""

def dichotomy(function_verif, left_born, rigth_born, precision):
    f = function_verif
    a = left_born
    b = rigth_born
    p = precision
    nbre_it = 0

    while ( abs( b - a ) > p ):
        nbre_it += 1
        middle = ( a + b )/2
        if ( f( middle )*f( b ) < 0):
            a = middle
        elif ( f( middle ) == 0 ):
            print( f"{a} est solution de l'équation")
            middle += p
        elif ( f( b ) == 0 ):
            print( f"{b} est solution de l'équation")
            b -= p
        else:
            b = middle
    return f"\nRESULTATS :\n\t[a,b] = [{a}, {b}]\n\tX_tilde = {(a+b)/2} à {p} près\n\tNombre d'itérations : {nbre_it}\nMéthode de Dichotomie terminée"

# def f(x):
#     return x*x + 7*x - 1.44

# print(dichotomy(f,-2,2,1e-10))