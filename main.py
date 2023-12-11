"""
    Author : Jules Dieu donné
    Date :
    Motif : the main file of the whole project
    Inputs : all the information we need to make this project work successfull
    Ouputs : the outputs of the each function
"""
from fx.dichotomy import dichotomy
from fx.corde import corde

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
    except:
        print("Veuillez entrer un chiffre")

if choix == 1:  # RESOLUTION D'EQUATION DE TYPE f(x) = 0

    def f(x):
        return  x*x + 7*x - 1.44
    
    def df(x):
        return 2*x + 7

    def F(x):
        return (1/3) * x**3 + (7/2) * x**2 - 1.44 * x
    
    def g(x):
        return 0

    print( "\n\t------------ [1] RESOLUTION DE f(x) = 0 ------------\n" )

    while True:
        print( "Veuillez saisir des informations nécessaires" )

        left_born = input( "Valeur de la borne à gauche de l'intervalle : " )
        rigth_born = input( "Valeur de la borne à droite de l'intervalle : " )
        precision = input( "Valeur de la tolérance : " )
        begin_value = input( "Première valeur de x : " )

        try:
            left_born = float( left_born )
            rigth_born = float( rigth_born )
            precision = float( precision )
            begin_value = float( begin_value )

            if rigth_born <= left_born:
                print( "Veuillez réssayer, valeur à droite inferieure ou égale à celle à gauche\nReprenez ;|" )
                continue
            else:
                if precision <= 0:
                    print( "La précision doit être supérieure à 0\nReprenez ;|" )
                else:
                    break
        except:
            print( "Valeur(s) saisie(s) incorrecte(s)\nReprenez ;|" )

    print( "\n\t------------------ (1) : Dichotomie / Bissection ------------------\n" )
    result_dichotomy = dichotomy( f, left_born, rigth_born, precision )
    print( result_dichotomy )

    print( "\n\t------------------ (1) : Dichotomie / Bissection ------------------\n" )
    result_corde = corde(f, left_born, rigth_born, precision, 10,000,000)
    print(result_corde)


# elif ( choix == 2 ):
#     continue

# elif ( choix == 3 ):
#     continue

# elif ( choix == 4 ):
#     continue

