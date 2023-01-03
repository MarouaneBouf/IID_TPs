import numpy as np

def cholesky(A):
    A = np.array(A, dtype=float)
    n, _ = A.shape
    L = np.zeros_like(A)
    for j in range(n):
        for i in range(j, n):
            if i == j:
                L[i, j] = np.sqrt(A[i, j] - np.sum(L[i, :j]**2))
            else:
                L[i, j] = (A[i, j] - np.sum(L[i:j] * L[j:j])) / L[j, j]
    return L

def solve_cholesky(L, b):
    L = np.array(L, dtype=float)
    b = np.array(b, dtype=float)
    n, _ = L.shape
    y = np.zeros(n)
    x = np.zeros(n)
    # Forward substitution:
    for i in range(n):
        sumj = sum(L[i, j] * y[j] for j in range(i))
        y[i] = (b[i] - sumj) / L[i, i]
    # Backward substitution:
    for i in range(n - 1, -1, -1):
        sumj = sum(L[j, i] * x[j] for j in range(i + 1, n))
        x[i] = (y[i] - sumj) / L[i, i]
    return x

A = np.array([[1, -1, 0, 0], [-1, 2, -1, 0], [0, -1, 2, -1], [0, 0, -1, 2]])
b = np.array([[1], [1], [1], [1]])

L = cholesky(A)
x = solve_cholesky(L, b)
print(f"Solution est la suivante : {x}")
