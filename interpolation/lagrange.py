"""
    Author : Jules Dieu donné
    Date : Monday, February 26, 2024
    Motif : 
    Inputs :    -

    Outputs :   *
"""

from scipy.interpolate import lagrange

def lagrange_interpolate(X, Y):
    return f"\nLe polynôme dd'interpolatino de Lagrange est :\n{lagrange(X, Y)}\n"

# X = [0,1,2]
# Y = [-2,0,3]
# X = [-2,-1,0,1]
# Y = [-7,4,1,2]
# print(lagrange_interpolate(X,Y))