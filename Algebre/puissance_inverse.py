import numpy as np

def largest_eigenvalue_inverse(A, v0, eps=1e-6):
  # Vérifie si A est inversible et si ses valeurs propres sont toutes positives
  if np.linalg.det(A) == 0:
    raise ValueError("A est inversible")
  if (np.linalg.eigvals(A) < 0).any():
    raise ValueError("A a une valeur propre negative")

  # Itère jusqu'à ce que v(k) converge
  v = v0
  while True:
    Av = np.linalg.inv(A).dot(v)
    v_next = Av / np.linalg.norm(Av)

    # Vérifie si v(k+1) a convergé
    if np.linalg.norm(v - v_next) < eps:
      break

    v = v_next

  return np.linalg.norm(A.dot(v)) / np.linalg.norm(v)

import numpy as np


def puissance_iterée_inverse(X0, A, LAMBDA):
  X = X0
  res=[]
  i = 0
  e = pow(10, -6)
  while i<3 or res[-1] - res[-2] != 0:
    Y = np.dot(np.linalg.inv(A - LAMBDA*np.eye(4)), X)
    X = np.divide(Y, np.linalg.norm(Y))
    sigma = LAMBDA + (1 / X.T.dot(Y))
    i += 1
    res.append(sigma)

  return min(res),i
  
  
# Teste la fonction avec la matrice donnée
A = np.array([[1, -1, 0, 0], [-1, 2, -1, 0], [0, -1, 2, -1], [0, 0, -1, 2]])
x0 = np.array([[0], [0], [0], [1]])

print(np.linalg.inv(A).dot(x0))
ans = puissance_iterée_inverse(x0, A, 0)
print(ans[0][0])
print(f"nombre d'iterations {ans[1]}")
