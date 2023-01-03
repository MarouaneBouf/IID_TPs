import numpy as np
from sympy import *





def f(x,A,b):
    x1=symbols('x1')
    x2=symbols('x2')
    x3=symbols('x3')
    x4=symbols('x4')
    x=np.array([[x1],[x2],[x3],[x4]])
    return 1/2*(np.dot(np.transpose(x),np.dot(A,x)))-np.dot(np.transpose(x),b)

x1=symbols('x1')
x2=symbols('x2')
x3=symbols('x3')
x4=symbols('x4')
x=np.array([[x1],[x2],[x3],[x4]])
A = np.array([[1, -1, 0, 0], [-1, 2, -1, 0], [0, -1, 2, -1], [0, 0, -1, 2]])
b = np.array([[1],[1],[1],[1]])
func = f(x,A,b)[0][0]


a = func.diff(x1)
b = func.diff(x2)
c = func.diff(x3)
d  = func.diff(x4)


def gradient(x):
    x1=x[0,0]
    x2=x[1,0]
    x3=x[2,0]
    x4=x[3,0]
    return - np.array([[eval(str(a))],[eval(str(b))],[eval(str(c))],[eval(str(d))]])

def ro(x,A):
    x1=x[0,0]
    x2=x[1,0]
    x3=x[2,0]
    x4=x[3,0]
    nrm=(np.linalg.norm(gradient(x),2))**2
    roo=nrm/np.dot(np.transpose(gradient(x)),np.dot(A,gradient(x)))
    return roo


x0=np.array([[0],[0],[0],[0]])
eps=0.00001
i = 0
while True:
    print(ro(x0,A)[0,0], gradient(x0),x0, sep='\n')
    print("------------")
    x1=x0+ro(x0,A)[0,0]*gradient(x0)
    if abs(x1[0,0]-x0[0,0])<eps and abs(x1[1,0]-x0[1,0])<eps and abs(x1[2,0]-x0[2,0])<eps and abs(x1[3,0]-x0[3,0])<eps :
        break
    x0=x1 
    i += 1
print(x1, i )

# import numpy as np
# import sympy
 
# A = np.array([[1, -1, 0, 0], [-1, 2, -1, 0], [0, -1, 2, -1], [0, 0, -1, 2]])
# b = np.array([[1],[1],[1],[1]])
# x = np.array([[0],[0],[0],[0]])
# x1=sympy.Symbol('x1')  
# x2=sympy.Symbol('x2')  
# x3=sympy.Symbol('x3')  
# x4=sympy.Symbol('x4')  


# x = np.array([[x1],[x2],[x3],[x4]])
# result = 0.5 * np.dot(x.T,np.dot(A, x)) - np.dot(x.T, b)
# print(result)