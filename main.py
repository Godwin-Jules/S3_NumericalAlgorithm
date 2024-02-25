"""
    Author : Jules Dieu donné
    Date :
    Motif : the main file of the whole project
    Inputs : all the information we need to make this project work successfull
    Ouputs : the outputs of the each function
"""

import numpy as np

from fx.dichotomy import dichoComplete
from fx.corde import corde
from fx.newton import newton
from fx.substitution import substitution

from ax.crout import crout

print("\t\t\t+-----------------------------------------+")
print("\t\t\t|         LES PROGRAMMES DE MTH_300       |")
print("\t\t\t+-----------------------------------------+\n")

print("\t\t_________________________ MENU _________________________\n")
print("\t[1] : RESOLUTION DE F(x) = 0")
print("\t[2] : RESOLUTION DE AX = B")
print("\t[3] : INTERPOLATION LINEAIRE")
print("\t[4] : EQUATION DIFFERENTIELLE\n")

while True:
    try:
        choix = input("Votre choix : ")
        choix = int(choix)
        if (1 <= choix & choix <= 4):
            break
        else:
            print("Veuillez entrer un choix valide")
    except Exception as e:
        print("Veuillez entrer un chiffre")
        print(e)

if choix == 1:  # RESOLUTION D'EQUATION DE TYPE f(x) = 0

    # def f(x):
    #     return  x*x + 7*x - 1.44
    
    # def df(x):
    #     return 2*x + 7

    # def F(x):
    #     return (1/3) * x**3 + (7/2) * x**2 - 1.44 * x
    
    # def g(x):
    #     return 0

    def f(x):
        return x*x + x + 1

    def df(x):
        return 2*x + 1
    
    def F(x):
        return (1/3)*x**3 + (1/2)*x*x + x

    print( "\n\t------------ [1] RESOLUTION DE f(x) = 0 ------------\n" )

    while True:
        print( "Veuillez saisir des informations nécessaires" )

        left_born = input( "Valeur de la borne à gauche de l'intervalle : " )
        rigth_born = input( "Valeur de la borne à droite de l'intervalle : " )
        precision = input( "Valeur de la tolérance : " )

        try:
            left_born = float( left_born )
            rigth_born = float( rigth_born )
            precision = float( precision )

            if rigth_born <= left_born:
                print( "Veuillez réssayer, valeur à droite inferieure ou égale à celle à gauche\nReprenez ;|" )
                continue
            else:
                if precision <= 0:
                    print( "La précision doit être supérieure à 0\nReprenez ;|" )
                else:
                    break
        except Exception as e:
            print( "Valeur(s) saisie(s) incorrecte(s)\nReprenez ;|" )
            print(e)

    try:
        print( "\n\t------------------ (1) : Dichotomie / Bissection ------------------\n" )

        # def verifier(function_verif, left_born, rigth_born, precision):
            
        # f = function_verif
        

        result_dichotomy = dichoComplete(f, left_born, rigth_born, precision)
        print(result_dichotomy)

    except Exception as e:
        print("Erreur lors de l'exécution de la méthode de Dichotomie")
        print(e)

    try:
        print("\n\t------------------ (2) : Sécante / Corde ------------------\n")

        result_corde = corde(f, left_born, rigth_born, precision, 1000000)
        print(result_corde)
    except Exception as e:
        print(e)

    try:
        print("\n\t------------------ (3) : Newton ------------------\n")

        result_newton = newton(f, df, left_born, precision, 1000000)
        print(result_newton)
    except Exception as e:
        print(e)
    
    """
    try:
        print("\n\t------------------ (4) : Balayage ------------------\n")

        result_scan = scan(f, left_born, rigth_born)
        print(result_scan)
    except Exception as e:
        print(e)
    """

    try:
        print("\n\t------------------ (4) : Substitution ------------------\n")

        result_substitution = substitution(f, left_born, precision, 1000000)
        print(result_substitution)
    except Exception as e:
        print(e)

elif choix == 2:      # RESOLUTION D'EQUATION DE TYPE Ax = b
    print("\n\t------------ [2] RESOLUTION DE AX = B ------------\n")

    # La matrice et le vecteur
    A = np.array([
        [4, -2, -3, 1],
        [1, 3, 1, 3],
        [1, 2, -1, -2],
        [2, 1, -1, -1]])
    b = np.array([20, 14, 3, 9])
    
    print(f"La matrice saisie est :\n", A)
    print(f"\nLe vecteur b saisie est :\n", b)

    if A.shape[0] != A.shape[1]:
        print("La matrice saisie n'est pas carrée")
    else:
        if A.shape[0] == b.shape[0]:
            try:
                print("\n\t------------------ (1) : Décomposition avec Crout ------------------\n")
                result_crout = crout(A, b)
                print(result_crout)
            except Exception as e:
                print(e)

            try:
                print("\n\t------------------ (2) : Décomposition avec Doolittle ------------------\n")
            except Exception as e:
                print(e)

            try:
                print("\n\t------------------ (3) : Méthode du pivot de Gauss ------------------\n")
            except Exception as e:
                print(e)

            try:
                print("\n\t------------------ (4) : Méthode de Gauss Seidel ------------------\n")
            except Exception as e:
                print(e)

            try:
                print("\n\t------------------ (5) : Méthode de Gauss Jordan ------------------\n")
            except Exception as e:
                print(e)

            try:
                print("\n\t------------------ (6) : Méthode de Jacobi ------------------\n")
            except Exception as e:
                print(e)

            try:
                print("\n\t------------------ (7) : Méthode de Cholevsky ------------------\n")
            except Exception as e:
                print(e)

            try:
                print("\n\t------------------ (8) : Méthode de  ------------------\n")
            except Exception as e:
                print(e)

elif choix == 3:    # LES INTERPOLATIONS
    print("\n\t------------ [3] INTERPOLATION LINEAIRE ------------\n")

    try:
        print("\n\t------------------ (1) : Méthode de Lagrange ------------------\n")
    except Exception as e:
        print(e)

    try:
        print("\n\t------------------ (2) : Méthode des Moindres carrés ------------------\n")
    except Exception as e:
        print(e)

    try:
        print("\n\t------------------ (3) : Méthode Newton ------------------\n")
    except Exception as e:
        print(e)


elif choix == 4:    # LES EQUATIONS DIFFERENTIELLES
    print("\n\t------------ [4] EQUATION DIFFERENTIELLE ------------\n")

    try:
        print("\n\t------------------ (1) : Méthode de Runge-Kutta ------------------\n")
    except Exception as e:
        print(e)

    try:
        print("\n\t------------------ (2) : Méthode d'Euler ------------------\n")
    except Exception as e:
        print(e)
