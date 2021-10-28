from random import randint
from sys import *

randomListe = [randint(0,99) for i in range(10)]

testList = [1,2,8,6,54,4,3]

def derivasort(liste:list) -> list:
    splitLists = splitList(liste, derive(liste))
    
    

def splitList(liste:list, sequences:list) -> list:
    count = 0
    liste.reverse()
    newLists: list[list] = [[]] #lists des listes
    for i in range(len(sequences)):
        if sequences[i] >= 0:
            newLists[count].append(liste.pop())
        if sequences[i] < 0:
            newLists.append([])
            count += 1
    return newLists


def derive(liste:list) -> list: #retourne une liste avec le sens de variation entre i et i+1
    newListe = []
    for i in range(len(liste) -1):
        newListe.append(liste[i+1] - liste[i])
    if newListe == []: newListe = [0]
    return newListe

def deriveToInfinity(liste:list) -> None: #cette fonction sert a rien mais elle est drole
    if len(liste) <= 1:
        return liste
    print(derive(liste))
    print(deriveToInfinity(derive(liste)))

print()