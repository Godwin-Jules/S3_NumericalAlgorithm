from dichotomy import dichotomy

def main_fx(f, df, F):

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
