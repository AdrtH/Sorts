from random import randint

randomListe = [randint(0,99) for i in range(10)]

testList = [1,2,8,6,54,4,3]

def derivasort(liste:list) -> list:
    listVariation = derive(liste) #liste ayant, à la place des elements, la différence entre 2 éléments
    for i in range(len(listVariation)):
        jsp



def derive(liste:list) -> list:
    newListe = []
    for i in range(len(liste) -1):
        newListe.append(liste[i+1] - liste[i])
    if newListe == []: newListe = [0]
    return newListe

def deriveToInfinity(liste:list) -> None:
    if len(liste) <= 1:
        return liste
    print(derive(liste))
    print(deriveToInfinity(derive(liste)))

print(derivasort())