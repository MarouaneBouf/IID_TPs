# TP 1 // PYTHON COURSE // IID_ENSA_2022_04_10

"""
# Ex1
a = int(input("Enter a ? "))
b = int(input("Enter b ? "))
print(f"La somme est {a+b} et la difference est {a-b}")
"""

"""
#Ex 2
euro = int(input())
x = "{:.2f}".format(euro*10.627)
print(f"Prix en euros {euro}\nPrix en dhs: {x}")
"""

"""
#Ex3
a = int(input("Enter a=? "))
b = int(input("Entrer b=? "))
print("La somme dépasse 100" if a+b>=100 else f"La somme est {a+b}")
"""
"""
#Ex4
print("Maximum de trois entiers")
a = int(input("1er entier: "))
b = int(input("2éme entier: "))
c = int(input("3éme entier: "))
print(f"Le maximum est {max(a,b,c)}")
"""
"""
#Ex5
a = int(input("Combien de 'la' pour l'écho? "))
print("Début: 'la'")
print("la"*a)
"""

#Ex6
while(True):
    n = float(input("Nombre: "))
    print("{:.2f}".format(n**2))
    x = input("Voulez vous recommencer? ")
    if x == "non":
        print("Au revoir")
        break


"""
while(True):
    n = int(input("Nombre impair: "))
    if(n%2):
        print("Merci")
        break
    print("J'ai demandé un nombre impair! Réssayez.")
"""
"""
s = list("AaelBc")
lower = [i for i in s if i.islower()]
upper = [i for i in s if i.isupper()]
for i in range(len(lower)-1):
    if lower[i] > lower[i+1]:
        lower[i],lower[i+1] = lower[i+1],lower[i]
for k in range(len(upper)-1):
    if upper[k] > upper[k+1]:
        upper[k],upper[k+1] = upper[k+1],upper[k]
print("".join(lower+upper))
"""
