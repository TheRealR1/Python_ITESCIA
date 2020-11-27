import string
import math
import itertools

# FONCTIONS

def exo1():
    nombre = int(input("Donnez un nombre : "))
    premierNombre = nombre
    while (nombre != 1 and nombre > 10):
        nombre = sommeCarre(listeChiffresPourNombre(nombre))
        print("Nombre ==>", nombre)
    if nombre == 1:
        print("Le nombre", premierNombre, "est un nombre porte bonheur!")
    else:
        print("Le nombre", premierNombre ,"n'est pas un nombre porte bonheur!")

def listeChiffresPourNombre(nombre):
    listeChiffre = []
    compteur = 1
    fini = False
    while(not fini):
        chiffre = int(((nombre % (10 * compteur)) - (nombre % (1 * compteur))) / (1 * compteur))

        if (chiffre == 0 and compteur > nombre):
            fini = True
        else:
            listeChiffre.insert(0, chiffre)
            compteur *= 10

    return listeChiffre

def sommeCarre(listeChiffre):
    somme = 0
    for chiffre in listeChiffre:
        somme += chiffre ** 2

    return somme

#exo1()

def exo2():
    nombre = int(input("Donnez un nombre : "))
    g2 = generateurG2(nombre)
    print(g2.__next__())

def generateurG():
    while True:
        yield list(string.ascii_lowercase)

def generateurG2(n):
    g = generateurG()
    while True:
        liste = []
        for i in range(0,n):
            liste += g.__next__()
        liste.sort()
        yield liste

#exo2()

def exo3():
    liste = [1,2,3]
    pow = powerset(liste)
    print(pow.__next__())

def powerset(A):
    while True:
        liste = []
        for i in range(0, len(A) + 1):
            liste += list(itertools.combinations(A,i))

        yield liste

#exo3()

def exo4():
    nombre = int(input("Donnez un nombre : "))

    for i in range(0,nombre):
        print(decoree())

def espionner(fonction):
    compteur = 0
    def imposteur():
        nonlocal compteur
        compteur += 1
        print("Appel de la fonction", fonction.__name__, "effectué", compteur, "fois.")
        return fonction()
    return imposteur

@espionner
def decoree():
    return "Je suis une fonction inutile"

exo4()
