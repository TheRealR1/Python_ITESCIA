import math
import itertools

# BREAKPOINT 1

def exo1():
    nom = input("Quel est votre nom ? ")
    print("Bienvenu ", nom, " !")

def exo2():
    a = int(input("Donnez un nombre : "))
    b = int(input("Donnez un nombre : "))
    print("Résultat : ", a + b)

def exo3():
    a = int(input("Donnez un nombre : "))
    b = int(input("Donnez un nombre : "))
    print("Maximum : ", max(a,b))

def exo4():
    a = int(input("Donnez un nombre : "))
    if a % 2 == 0:
        print("Nombre pair")
    else:
        print("Nombre impair")

def exo5():
    a = int(input("Donnez votre age : "))
    if a < 18:
        print("Vous êtes mineur")
    else:
        print("Vous êtes majeur")

def exo6():
    a = int(input("Donnez un nombre : "))
    b = int(input("Donnez un nombre : "))
    c = int(input("Donnez un nombre : "))
    print("Maximum : ", max(a, b, c))

#exo1()
#exo2()
#exo3()
#exo4()
#exo5()
#exo6()

# BREAKPOINT 2

def exo7():
    for i in range(0, 100):
        print(i + 1)

def exo8():
    n = 0
    a = int(input("Donnez un nombre : "))
    for i in range(0, a):
        n += i + 1
    print("Somme : ", n)

def exo9():
    n = 1
    a = int(input("Donnez un nombre : "))
    for i in range(0, a):
        n *= i + 1
    print("Factorielle : ", n)

def exo10():
    a = int(input("Donnez le rayon : "))
    print("Surface : ", a**2 * math.pi)
    print("Périmètre : ", a * 2 * math.pi)

def exo11():
    a = int(input("Donnez un nombre : "))
    print("Les diviseurs de ", a, " sont :")
    for i in range(0, a):
        if a % (i + 1) == 0:
            print(i + 1)

#exo7()
#exo8()
#exo9()
#exo10()
#exo11()

# BREAKPOINT 3

def exo12():
    n = int(input("Donnez un nombre : "))
    for i in range(0, 10):
        print(n * (i + 1))

    #Amelioration
    for i in range(0, 9):
        print("Table de ", (i + 1))
        for j in range(0, 10):
            print((i + 1) * (j + 1))

def exo13():
    a = int(input("Donnez un nombre : "))
    b = int(input("Donnez un nombre : "))
    print("Quotient : ", a // b)
    print("Reste division euclidienne : ", a % b)

def exo14():
    a = int(input("Donnez un nombre : "))
    est_cp = False
    for i in range(0, a):
        if (i + 1)**2 == a:
            est_cp = True
            print(a, " est carré parfait de ", (i + 1))
    if not est_cp:
        print(a, " n'est pas carré parfait")

def exo15():
    a = int(input("Donnez un nombre : "))
    est_premier = False
    for i in range(1, a - 1):
        if a % (i + 1) == 0:
            est_premier = True
    if a == 1 or est_premier:
        print(a, "est premier.")
    else:
        print(a, "n'est pas premier")

#exo12()
#exo13()
#exo14()
#exo15()

#BREAKPOINT 4

def exo16():
    s = "Python"
    for car in s:
        print(car)

def exo17():
    s = "itescia.fr"
    compteur = []
    caracteres = []
    for car in s:
        car_trouve = False
        for i in range(0, len(caracteres)):
            if car == caracteres[i]:
                car_trouve = True
                compteur[i] = compteur[i] + 1
        if not car_trouve:
            compteur.append(1)
            caracteres.append(car)

    for i in range(0, len(caracteres)):
        print("Le caractère : \"", caracteres[i] ,"\" figure", compteur[i] ,"fois dans la chaine", s)

def exo18():
    lettre = 'a'
    chaine = input("Votre chaine : ")
    for i in range(0, len(chaine)):
        if chaine[i] == lettre:
            print("La lettre ‘", lettre ,"’ se trouve à la position : ", i)

def exo19():
    l = ["laptop", "iphone", "tablet"]
    for chaine in l:
        print(",".join(chaine))
        print("Longueur de la chaine : ", len(chaine))

def exo20():
    chaine = input("Votre chaine : ")
    new_chaine = "" + chaine[len(chaine) - 1]
    for i in range(1, len(chaine) - 1):
        new_chaine += chaine[i]
    new_chaine += chaine[0]
    print(new_chaine)

def exo21():
    voyelles = ['a', 'e', 'i', 'o', 'u', 'y']
    chaine = input("Votre chaine : ")
    compteur = 0
    for car in chaine:
        for voy in voyelles:
            if car == voy:
                compteur += 1
    print("La chaine \"", chaine ,"\" possède", compteur,"voyelles.")

#exo16()
#exo17()
#exo18()
#exo19()
#exo20()
#exo21()

#BREAKPOINT 5

def exo22():
    chaine = input("Votre chaine : ")
    tab = chaine.split(" ")
    print("La premier mot est \"", tab[0], "\".")

def exo23():
    chaine = input("Votre chaine : ")
    tab = chaine.split(".")
    print("L’extension du fichier est .", tab[len(tab) - 1])

def exo24():
    chaine = input("Votre chaine : ")
    fin_moitie = math.floor(len(chaine) / 2)
    est_pal = True
    for i in range(0, fin_moitie):
        if not chaine[i] == chaine[len(chaine) - 1 - i]:
            est_pal = False
    if est_pal:
        print(chaine ,"est un palindrome.")
    else:
        print(chaine, "n'est pas un palindrome.")

def exo25():
    chaine = input("Votre chaine : ")
    new_chaine = ""
    for i in range(0, len(chaine)):
        new_chaine += chaine[len(chaine) - 1 - i]
    print(new_chaine)

def exo26():
    lettre = 'a'
    chaine = input("Votre chaine : ")
    tab = chaine.split(" ")
    print("Tous les mots commençant par la lettre", lettre, "sont : ")
    for chaine in tab:
        if (chaine[0] == lettre):
            print("Le mot \"", chaine ,"\" commencent par la lettre ", lettre)

#exo22()
#exo23()
#exo24()
#exo25()
#exo26()

#BREAKPOINT 6

def exo27():
    chaine = input("Votre chaine : ")
    tab = chaine.split(" ")
    index_max = 0
    for i in range(0, len(tab)):
        if len(tab[i]) > len(tab[index_max]):
            index_max = i
    print("Le mot le plus long est \"", tab[index_max], "\"")

def exo28():
    tab = []
    if len(tab) == 0:
        print("La liste est vide")
    else:
        print("La liste contient des éléments")

    chaine = ""
    if chaine == "":
        print("La chaine est vide")
    else:
        print("La chaine contient des caractères")

def exo29():
    tab = ["ceci","est","une","est", "liste"]
    new_tab = []
    for i in range(0, len(tab)):
        est_trouve = False
        for chaine in new_tab:
            if chaine == tab[i]:
                est_trouve = True
        if not est_trouve:
            new_tab.append(tab[i])
    print(new_tab)

def exo30():
    tab = ["c'est", "une", "liste"]
    tab2 = ["ce", "n'est", "pas", "une", "liste"]
    est_trouve = False
    for chaine in tab:
        for chaine2 in tab2:
            if chaine == chaine2:
                est_trouve = True
    if est_trouve:
        print("Les deux listes ont une valeur commune")
    else:
        print("Les deux listes n'ont pas de valeurs communes")

def exo31():
    tab = [0,2,5,9,3,4,2,8]
    pair = []
    impair = []
    for nb in tab:
        if nb % 2 == 0:
            pair.append(nb)
        else:
            impair.append(nb)
    print("Pair : ", pair)
    print("Impair : ", impair)

def exo32():
    tab = ["ceci", "est", "une", "liste"]
    print(list(itertools.permutations(tab)))

def exo33():
    chaine = input("Votre chaine : ")
    new_chaine = ""
    for i in range(0, len(chaine)):
        if i % 2 == 0:
            new_chaine += chaine[i]
    print(new_chaine)

def exo34():
    notes = [12,4,14,11,18,13,7,10,5,9,15,8,14,16]
    new_notes = []
    for note in notes:
        if note >= 10:
            new_notes.append(note)
    print(new_notes)

def exo35():
    chaine = input("Votre chaine : ")
    tab = chaine.split(" ")
    listDic = []
    compteur = []
    mots = []

    for mot in tab:
        mot_trouve = False
        for i in range(0, len(listDic)):
            if mot == listDic[i].get("mot"):
                mot_trouve = True
                listDic[i]["compteur"] = listDic[i].get("compteur") + 1
        if not mot_trouve:
            listDic.append({"compteur": 1, "mot": mot})

    for i in range(0, len(listDic)):
        print("Le mot : \"", listDic[i].get("mot") ,"\" figure", listDic[i].get("compteur") ,"fois dans la chaine \"", chaine, "\".")

def exo36():
    chaine = input("Votre chaine : ")
    tab = chaine.split()
    new_chaine = ""
    for mot in tab:
        new_chaine += mot + " "
    print(new_chaine)

def exo37():
    chaine = input("Votre chaine : ")
    chaine2 = input("Votre chaine : ")
    tab = chaine.split()
    tab2 = chaine2.split()
    new_tab = []
    for mot in tab:
        for mot2 in tab2:
            if (mot == mot2 and mot not in new_tab):
                new_tab.append(mot)
    print(new_tab)

def exo38():
    s = "Python est un langage de programmation"
    tab = s.split(" ")
    new_chaine = "" + tab[len(tab) - 1]
    for i in range(1, len(tab) - 1):
        new_chaine += " " + tab[i]
    new_chaine += " " + tab[0]
    print(new_chaine)

def exo39():
    chaine = input("Votre chaine : ")
    tab = chaine.split(" ")
    compteur = 0
    for mot in tab:
        compteur += 1
    print("Nombre de mots : ", compteur)

#exo27()
#exo28()
#exo29()
#exo30()
#exo31()
#exo32()
#exo33()
#exo34()
#exo35()
#exo36()
#exo37()
#exo38()
#exo39()

#BREAKPOINT 8

def exo41():
    n = 3
    tab = [2,5,9,3,4,2,8]
    print("Nombre d'entier dans", tab ," divisible par", n ,":", nombreDivisibles(tab, n))

def nombreDivisibles(entiers, n):
    compteur = 0
    for entier in entiers:
        if entier % n == 0:
            compteur += 1
    return compteur

def exo42():
    n = 2
    tab = [2, 5, 9, 3, 4, 2, 8]
    print("Nombre d'occurence de ", n ," dans", tab, ":", nombreOccurences(tab, n))

def nombreOccurences(liste, element):
    compteur = 0
    for elmt in liste:
        if element == elmt:
            compteur += 1
    return compteur

def exo43():
    chaine = input("Votre chaine : ")
    print(insertEtoiles(chaine))

def insertEtoiles(chaine):
    new_chaine = "" + chaine[0]
    for i in range(1, len(chaine)):
        new_chaine += "*" + chaine[i]
    return new_chaine

def exo44():
    L = ["Python", "est", "un", "langage", "de", "programmation"]
    print(toutEnMajuscules(L))

def toutEnMajuscules(liste):
    listeMaj = []
    for mot in liste:
        listeMaj.append(mot.upper())
    return listeMaj

def exo45():
    chaine = input("Votre chaine : ")
    res = nombreMinMaj(chaine)
    print("Le nombre de majuscules est : ", res[0])
    print("Le nombre de minuscules est : ", res[1])

def nombreMinMaj(chaine):
    compteurMin = 0
    compteurMaj = 0
    for car in chaine:
        if car.isupper():
            compteurMaj += 1
        elif car.islower():
            compteurMin += 1
    return (compteurMin, compteurMaj)

def exo46():
    nombre = 12334
    print("Les chiffres pour le nombre", nombre ,"sont :", listeChiffresPourNombre(nombre))

def listeChiffresPourNombre(nombre):
    listeChiffre = []
    compteur = 1
    fini = False
    while(not fini):
        chiffre = int(((nombre % (10 * compteur)) - (nombre % (1 * compteur))) / (1 * compteur))

        if (chiffre == 0):
            fini = True
        else:
            listeChiffre.insert(0, chiffre)
            compteur *= 10

    return listeChiffre

def exo47():
    chaine = input("Votre chaine : ")
    chaine2 = input("Votre chaine : ")

    print(motsCommuns(chaine, chaine2))

def motsCommuns(chaine, chaine2):
    tab = chaine.split()
    tab2 = chaine2.split()
    new_tab = []
    for mot in tab:
        for mot2 in tab2:
            if (mot == mot2 and mot not in new_tab):
                new_tab.append(mot)
    return new_tab

#exo41()
#exo42()
#exo43()
#exo44()
#exo45()
exo46()
#exo47()