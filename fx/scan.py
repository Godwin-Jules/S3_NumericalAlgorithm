"""
    Author : Jules Dieu donné
    Date : Tuesday, December 5, 2023
    Motif : equation solving by Scanning (Bissection) method
    Inputs :    - the function to verify
                - the limits of the interval [a, b]

    Outputs :   * the solution intervals [a, b]
                * the exact solutions if possible
"""

def scan( function_verif, left_born, rigth_born):
    sol_intervals = []
    sol_points = []
    step = 0.5
    f = function_verif
    a, b = left_born, left_born

    if( f( left_born ) * f( rigth_born ) < 0 ):
        print( "Nombre pair de solution" )
    elif( f( left_born ) * f( rigth_born ) > 0 ):
        print( "Nombre impair de solution" )
    
    while( b < rigth_born ):
        b = a + step
        if ( f( a )*f( b ) < 0 ):
            sol_intervals.append( [a,b] )
            print( "un intervalle de solution localisé" )
        elif( f( a ) == 0 ):
            sol_points.pop( a )
            print( "une solution exacte trouvée" )
        elif( f( b ) == 0 ):
            sol_points.append( b )
        a = b

    print( "\nAffichage des résultats de balayage" )
    if ( len(sol_intervals) == 0 ):
        print( "Pas d'intervalle solution" )
    else:
        print( "Les intervalles solution sont :" )
        i = 1
        for interval in sol_intervals:
            print( f"{i} => [{interval[0]}, {interval[1]}]" )
            i+=1
    
    if ( len(sol_points) == 0 ):
        print( "\nPas de solution exacte trouvée" )
    else:
        print( "\nLes solutions exactes trouvées sont :" )
        i = 1
        for point in sol_points:
            print( f"{i} => {point}" )
            i+=1

# def f(x):
#     return x*x + 7*x - 1.44

# scan(f,-2,2)