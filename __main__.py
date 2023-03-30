import random

##jeu de  nombre aleatoire
print("********Jouons**********")
print("veillez saisir un premier nombre")
nombre_1=input()

print("veillez saisir un deuxieme nombre")
nombre_2=input()

# le nombre a trouver doit etre compris entre les nombre 1 et nombre 2
nombre=int(random.randint(int(nombre_1),int(nombre_2)))
print("Trouver un nombre compris entre ", nombre_1, "et ", nombre_2 )
n=input()

while n!=nombre:
    if int(n) >nombre:
        print("c'est plus petit")
        n=input()
    elif int(n)<nombre:
        print("plus grand") 
        n=input()
    else:
        break
    
print("Bravo! Vous avez trouve")
print("nombre = ", nombre)