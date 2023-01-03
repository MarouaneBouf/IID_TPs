import numpy as np

A = np.array([[1, -1, 0, 0], [-1, 2, -1, 0], [0, -1, 2, -1], [0, 0, -1, 2]])

D=np.array([[1,0,0,0],[0,2,0,0],[0,0,2,0],[0,0,0,2]])
E=np.array([[0,0,0,0],[1,0,0,0],[0,1,0,0],[0,0,1,0]])
F=np.array([[0,1,0,0],[0,0,1,0],[0,0,0,1],[0,0,0,0]])

w = float(input("entrer facteur de relaxation w: "))
x0 = np.array([[0],[0],[0],[0]])
b = np.array([[1],[1],[1],[1]])
A_1 = np.array(A)

# The solution of the system Ax=b
print(np.linalg.inv(A_1)@b)
print(D-E-F)



i = 0
eps=(10)**(-10)

while True:
    x1=np.dot(np.dot(np.linalg.inv(D-w*E),(1-w)*D+w*F),x0) +  w*np.dot(np.linalg.inv(D-w*E),b)
    if abs(x1[0,0]-x0[0,0])<eps and abs(x1[1,0]-x0[1,0])<eps and abs(x1[2,0]-x0[2,0])<eps and abs(x1[3,0]-x0[3,0])<eps:
        break
    x0=x1
    i+=1
    
print("la solution est : \n",x1)
print("le nombre d'iterations :",i)
