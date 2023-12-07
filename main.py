"""
    Author : Jules Dieu donné
    Date :
    Motif : the main file of the whole project
    Inputs : all the information we need to make this project work successfull
    Ouputs : the outputs of the each function
"""


from fx.main_fx import main_fx

sys.path.append("fx/main_fx")

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
        return x * x + 7 * x - 1.44


    def df(x):
        return 2 * x + 7


    def F(x):
        return

    main_fx(f, df, F)

# elif ( choix == 2 ):
#     continue

# elif ( choix == 3 ):
#     continue

# elif ( choix == 4 ):
#     continue

print( "\t\t\t+-----------------------------------------+" )
print( "\t\t\t|         LES PROGRAMMES DE MTH_300       |" )
print( "\t\t\t+-----------------------------------------+\n" )

print( "\t\t_________________________ MENU _________________________\n" )
print( "\t[1] : RESOLUTION DE F(x) = 0" )
print( "\t[2] : RESOLUTION DE AX = B" )
print( "\t[3] : INTERPOLATION LINEAIRE" )
print( "\t[4] : EQUATION DIFFERENTIELLE\n" )

while True:
    try:
        choix = input( "Votre choix : " )
        choix = int( choix )
        if ( 1 <= choix & choix <= 4 ):
            break
        else:
            print( "Veuillez entrer un choix valide" )
    except:
        print( "Veuillez entrer un chiffre" )

