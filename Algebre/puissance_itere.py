

import numpy as np

def iterative_power(A, X0, eps=1e-6):
    X = X0
    # Pour stocker les valeurs propres
    res = []
    i = 0
    while i < 2 or abs(res[-1] - res[-2])!=0: 
        Y = A.dot(X)
        X = Y/np.linalg.norm(Y)
        sigma = X.T.dot(Y)
        res.append(sigma)
        i += 1
        print(f"Iteration {i + 1}, sigma = {sigma}")
        
        
# Teste la fonction avec la matrice donnée
A = np.array([[1, -1, 0, 0], [-1, 2, -1, 0], [0, -1, 2, -1], [0, 0, -1, 2]])
x0 = np.ones(4)
iterative_power(A, x0)