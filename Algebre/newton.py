import math
from sympy import symbols
import numpy as np

# Definition of the system 
def fonction(x, y):
    f1 = x**2 - y # First equation
    f2 = y**2 # Second equation
    return np.matrix([[f1], [f2]])

x = symbols('x')
y = symbols('y') 

def invers_jacobienne(x, y): # Function to calculate Jacobian matrix and its inverse
    jac = np.matrix([[2*x, -1], [0, 2*y]])
    inv = np.linalg.inv(jac)
    return [jac, inv] 

x0, y0 = 1, 1
jacob, invers = invers_jacobienne(x0, y0)
print('det(jacob) =', np.linalg.det(jacob)) # det(jacob) = 4, so it is invertible and the method will converge

eps = 0.0001 # Error
i = 0
maxiteration = 10000
while (
    abs(fonction(x0, y0)[0]) > eps or abs(fonction(x0, y0)[1]) > eps
) and maxiteration > i:
    systeme = fonction(x0, y0)
    valeur = np.matrix([[x0], [y0]]) - invers@systeme # Newton method
    x0, y0 = float(valeur[0]), float(valeur[1])
    i += 1


systeme = fonction(1, 1)
print(np.matrix([[1], [1]]) - invers@systeme)
print("--------------------")
print(fonction(x0, y0))
print("Solutions at iteration", i, ": X", i, "=", x0, ", Y", i, "=", y0)
