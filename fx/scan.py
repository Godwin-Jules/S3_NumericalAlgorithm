"""
    Author : Jules Dieu donné
    Date : unknown
    Motif : equation solving by Scanning (Bissection) method
    Inputs :    - the function to verify
                - the limits of the interval [a, b]

    Outputs :   * the solution intervals [a, b]
                * the exact solutions if possible
"""

def scan( function_verif, left_born, rigth_born):
    sol_intervals = {}
    sol_points = {}
    step = 0.5
    f = function_verif
    a = left_born

    if( f( left_born ) * f( rigth_born ) < 0 ):
        print( "Nombre pair de solution" )
    elif( f( left_born ) * f( rigth_born ) > 0 ):
        print( "Nombre impair de solution" )
    
    while( b < rigth_born ):
        b = a + step
        if ( f( a )*f( b ) < 0 ):
            sol_intervals.pop( {a, b} )
            print( "un intervalle de solution localisé" )
        elif( f( a ) == 0 ):
            sol_points.pop( a )
            print( "une solution exacte trouvée" )
        elif( f( b ) == 0 ):
            sol_points.pop( b )
        
        a = b
    print( "Affichage des résultats de balayage" )
    if ( sol_intervals.size() == 0 ):
        print( "Pas d'intervalle solution" )
    else:
        print( "Les intervalles solution sont :" )
        i = 1
        for interval in sol_intervals:
            print( i + " " + interval )
            ++i
    
    if ( sol_points.size() == 0 ):
        print( "Pas de solution exacte trouvée" )
    else:
        print( "Les solutions exactes trouvées sont :" )
        i = 1
        for point in sol_points:
            print( i + " " + point )
            ++i