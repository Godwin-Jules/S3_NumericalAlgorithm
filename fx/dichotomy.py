"""
    Author : Jules Dieu donné
    Date : Tuesday, December 5, 2023
    Motif : equation solving by Dichotomy (Bissection) method
    Inputs :    - the function to verify
                - the limits of the interval [a, b]
                - the precision p (tolerance)
                - the maximum number of iteration

    Outputs :   * the solution interval [a, b]
                * the x tilde value
                * number of iterations
"""

# def verifier(function_verif, left_born, rigth_born, precision):
    
#     f = function_verif
#     a, b = left_born, left_born
#     nb_solution = 0
#     amplitude = abs(rigth_born - left_born)
#     pas = amplitude/10

#     while b < rigth_born:
#         b = a + pas
#         if(f(a)*f(b) < 0):
#             nb_solution += 1
#             if (nb_solution == 1):
#                 print(dichotomy(f, a, b, precision))
#     if(nb_solution > 1):
#         print(f"\nAu total {nb_solution} solutions")

def dichoComplete(f, left_born, right_born, precision):
    a, b = left_born, left_born
    nb_solution = 0
    amplitude = abs(right_born - left_born)
    pas = (amplitude / 5)
    
    while b < right_born:
        b = a + pas
        if f(a) * f(b) <= 0:
            nb_solution += 1
            dichoResult = dichotomy(f, a, b, precision)
            print(dichoResult)
            a = b
        else:
            a = b
            continue

    if nb_solution >= 1:
        return f"\nAu total {nb_solution} solution(s)"
    else:
        return f"\nPas de solution avec la méthode de dichotomie !"


def dichotomy(function_verif, left_born, rigth_born, precision):
    f = function_verif
    a = left_born
    b = rigth_born
    p = precision
    nbre_it = 0

    if f(a)*f(b) > 0:
        return "Pas de solution dans cet intervalle"
    else:
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
    return f"\nRESULTATS :\n\t[a,b] = [{a}, {b}]\n\tX_tilde = {(a+b)/2}\n\tNombre d'itérations : {nbre_it}\nMéthode de Dichotomie terminée"

# def f(x):
#     return x*x + 7*x - 1.44

# print(dichotomy(f,-2,2,1e-10))