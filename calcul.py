from math import sqrt
from tkinter import *


# solutions si delta > 0
def deltaPositive(a, b, delta):
    x1 = ((-1 * b) - sqrt(delta)) / (2 * a)
    x2 = ((-1 * b) + sqrt(delta)) / (2 * a)
    return (x1, x2)


# solutions si delta = 0
def deltaZero(a, b):
    x = (-1 * b) / (2 * a)
    return x


# calcul de delta
def deltaCatch(a, b, c):
    delta = (b ** 2) - 4 * a * c
    return delta


# calcul de alpa
def alpaCatch(a, b):
    alpha = (-b) / (2 * a)
    return alpha


# calcul de beta
def betaCatch(a, b, c, alpha):
    beta = (a * alpha**2) + (b * alpha) + c
    return beta


# retour des solutions selon la valeur de delta
def deltaTest(delta, a, b):
    if delta > 0:
        S = deltaPositive(a, b, delta)
    elif delta == 0:
        S = deltaZero(a, b)
    else:
        S = None
    return S


# récupération de a, b et c (sous forme de tuple)
def userVar():
    var = ['a', 'b', 'c']
    inputs = ()
    for i in var:
        inputs += (int(input(f'Valeur de {i} :\n> ')),)
    return inputs


# reformate le string selon une liste de char définie
def formatResult(result, charList):
    for i in charList:
        result = result.replace(i, "")
    return result

# affichage du résultat
def main(a, b, c):
    charList = ["(", ")"]
    delta = deltaCatch(a, b, c)
    S = formatResult(str(deltaTest(delta, a, b)), charList)
    print(f'S = {{{S}}}')

# affichage du tableau de variation
def tkVariationTable(a, b, c, alpha, beta):

    # première ligne, première colonne
    def A1f():
        A1 = Canvas(variationTable, width=100, height=100, background='white', borderwidth=3)
        txtA1 = A1.create_text(50, 50, text="x", font="Arial 25 italic")
        A1.grid(row=1, column=1)

    # seconde ligne, première colonne
    def B1f():
        B1 = Canvas(variationTable, width=100, height=100, background='white', borderwidth=3)
        txtB1 = B1.create_text(50, 50, text="f(x)", font="Arial 25 italic")
        B1.grid(row=2, column=1)

    # première ligne, seconde colonne
    def A2f(alpha):
        alpha = round(alpha, 2)  # on garde que 2 décimales pour l'affichage
        A2 = Canvas(variationTable, width=500, height=100, background='white', borderwidth=3)
        txtA2 = A2.create_text(50, 50, text="-∞", font="Arial 25 italic")

        txtA3 = A2.create_text(225, 50, text=alpha, font="Arial 25 italic")

        txtA4 = A2.create_text(450, 50, text="+∞", font="Arial 25 italic")

        A2.grid(row=1, column=2)

    # seconde ligne, seconde colonne
    def B2f(beta, a):
        beta = round(beta, 2) # on garde que 2 décimales pour l'affichage

        # flèche de gauche descendente
        def B2ArrowDown():
            B2LineDown = B2.create_line(25, 25, 150, 70)
            B2ArrowDown = B2.create_line(150, 70, 125, 75)
            B2ArrowUp = B2.create_line(150, 70, 125, 50)

        # flèche de gauche montante
        def B2ArrowUp():
            B2LineUp = B2.create_line(25, 70, 150, 25)
            B2ArrowDown = B2.create_line(150, 25, 125, 20)
            B2ArrowUp = B2.create_line(150, 25, 135, 48)

        # flèche de droite descendente
        def B4ArrowDown():
            B4LineDown = B2.create_line(325, 25, 450, 70)
            B4ArrowDown = B2.create_line(450, 70, 425, 75)
            B4ArrowUp = B2.create_line(450, 70, 425, 50)

        # flèche de droite montante
        def B4ArrowUp():
            B4LineUp = B2.create_line(325, 70, 450, 25)
            B4ArrowDown = B2.create_line(450, 25, 425, 20)
            B4ArrowUp = B2.create_line(450, 25, 435, 48)

        #flèche montante à gauche et descendante à droite
        def increasingFunction():
            B2ArrowUp()
            B4ArrowDown()

        # flèche descendante à gauche et montante à droite
        def decreasingFunction():
            B2ArrowDown()
            B4ArrowUp()

        B2 = Canvas(variationTable, width=500, height=100, background='white', borderwidth=3)

        if(a < 0 ): # si a < 0 fonction croissante
            decreasingFunction()
            B3txt = B2.create_text(225, 70, text=beta, font="Arial 25 italic")
        else: # sinon décroissante
            increasingFunction()
            B3txt = B2.create_text(225, 25, text=beta, font="Arial 25 italic")

        B2.grid(row=2, column=2)

    window = Tk() # création de la fenêtre
    window.title("Tableau de variation")
    variationTable = Frame(window, width=600, height=200, background='black') # frame contenant le tout

    # affichage de chaque parties du tableau
    A1f()
    B1f()
    A2f(alpha)
    B2f(beta, a)

    variationTable.pack(side=LEFT)
    window.mainloop()


tupleValues = userVar() # récupération d'un tuple contenant a, b, c
# on sort les valeurs du tuple
a = tupleValues[0]
b = tupleValues[1]
c = tupleValues[2]

alpha = alpaCatch(a, b)
beta = betaCatch(a, b, c, alpha)
main(a, b, c) # résoltion de l'équation
tkVariationTable(a, b, c, alpha, beta) # tableau de variation


