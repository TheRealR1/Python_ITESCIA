import math
import itertools

# CLASSES

def exo1():
    d = Domino(4, 6)
    d.affiche_points()
    x = d.totale()
    print("Somme :", x)

class Domino:
    def __init__(self, faceA, faceB):
        self.faceA = faceA
        self.faceB = faceB

    def affiche_points(self):
        print("Face A :", self.faceA, "| Face B :", self.faceB)

    def totale(self):
        return self.faceA + self.faceB

    def __repr__(self):
        return "Domino = " \
               "\n\tfaceA : {}" \
               "\n\tfaceB : {}".format(self.faceA, self.faceB)

#exo1()

def exo2():
    print("")
    compte1 = CompteBancaire("Jean", 1000)
    compte1.retrait(200)
    compte1.affiche()
    compte2 = CompteBancaire("Marc")
    compte2.depot(500)
    compte2.affiche()

class CompteBancaire:
    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire
        self.solde = solde

    def retrait(self, retrait):
        self.solde -= retrait

    def depot(self, depot):
        self.solde += depot

    def affiche(self):
        print("Le solde du compte de", self.titulaire, "est de", self.solde, "euros.")

    def __repr__(self):
        return "CompteBancaire = " \
               "\n\ttitulaire : \"{}\"" \
               "\n\tsolde : {}€".format(self.titulaire, self.solde)

#exo2()

def exo3():
    tab = TableMultiplication(3)
    tab.prochain()
    tab.prochain()
    tab.prochain()
    tab.prochain()

class TableMultiplication:
    compteur = 0

    def __init__(self, nombre):
        self.nombre = nombre

    def multi(self, compteur):
        while True:
            yield (compteur * self.nombre)

    def prochain(self):
        m = self.multi(self.compteur)
        self.compteur += 1
        print(m.__next__())

    def __repr__(self):
        return "TableMultiplication = " \
               "\n\tnombre : {}".format(self.nombre)

#exo3()

def exo4():
    f = Fraction(3, 4)
    f.affiche()
    g = Fraction(1, 2)
    g.affiche()
    r1 = f + g
    r1.affiche()
    r2 = f / g
    r2.affiche()
    r3 = f * g
    r3.affiche()
    r4 = f - g
    r4.affiche()

class Fraction:
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom

    def affiche(self):
        print(self.num, "/", self.denom)

    def __add__(self, fraction2):
        numFinal = (self.num * fraction2.denom) + (self.denom * fraction2.num)
        denomFinal = self.denom * fraction2.denom
        div = math.gcd(numFinal, denomFinal)

        return Fraction(int(numFinal / div), int(denomFinal / div))

    def __sub__(self, fraction2):
        numFinal = (self.num * fraction2.denom) - (self.denom * fraction2.num)
        denomFinal = self.denom * fraction2.denom
        div = math.gcd(numFinal, denomFinal)

        return Fraction(int(numFinal / div), int(denomFinal / div))

    def __mul__(self, fraction2):
        numFinal = self.num * fraction2.num
        denomFinal = self.denom * fraction2.denom
        div = math.gcd(numFinal, denomFinal)

        return Fraction(int(numFinal / div), int(denomFinal / div))

    def __truediv__(self, fraction2):
        #On inverse
        numFinal = self.num * fraction2.denom
        denomFinal = self.denom * fraction2.num
        div = math.gcd(numFinal, denomFinal)

        return Fraction(int(numFinal / div), int(denomFinal / div))

    def __repr__(self):
        return "Fraction = " \
               "\n\t{}/{}".format(self.num, self.denom)

#exo4()

def exo5():
    d = Domino(3,4)
    print(d)
    cb = CompteBancaire("Erwan",123)
    print(cb)
    table = TableMultiplication(3)
    print(table)
    f = Fraction(1,2)
    print(f)
    p = Poly(1,2,3)
    print(p)

#exo5()

def exo6():
    p = Poly(3, 4, -2)
    print(p.coeff)
    print(p.evalue(2))
    p1 = Poly(1, 4)
    p2 = Poly(3, -3, 2)
    p3 = p1 + p2
    print(p3.coeff)

class Poly:
    def __init__(self, *args):
        self.coeff = []
        for c in args:
            self.coeff.append(c)

    def evalue(self, x):
        somme = self.coeff[0]
        for i in range(1,len(self.coeff)):
            somme += (self.coeff[i] * (x ** i))
        return somme

    def __repr__(self):
        return "Poly = " \
               "\n\t{}/{}".format(self.coeff)

    def __add__(self, poly2):
        polyFinal = []
        zip = list(itertools.zip_longest(self.coeff, poly2.coeff,fillvalue=0))
        for i in range(0, len(zip)):
            polyFinal.append((zip[i][0] + zip[i][1]))

        return Poly(polyFinal)

exo6()