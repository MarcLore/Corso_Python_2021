#Date in input due liste di elementi da terminale lunghe n1 e n2, stampare una lista in output 
#che sia la differenza della prima con la seconda.
def Esercizio1():
    lista1 = []
    lista2 = []
    lista3 = []

    contatore = 0
    while contatore < 6:
        if contatore < 4:
            n1 = input("Inserisci elemento Lista 1: ")
            contatore = contatore + 1
            lista1.append(n1)

        else:
            n2 = input("Inserisci elemento Lista 2: ")
            contatore = contatore + 1
            lista2.append(n2)

    #SOLUZIONE1
    #for elemento in lista2:                        #Per ogni elemento in lista2
        #while elemento in lista1:                  #finchè elemento nella lista1
            #lista1.remove(elemento1)               #rimuovi il primo elemento nella lista.
    #print(lista1)

    #SOLUZIONE2
    for elemento1 in lista1:                         #Per ogni elemento in lista1:
        if elemento1 not in lista2:                  #se elemento non è in lista2,
            lista3.append(elemento1)                 #inserisci l'elemento nella lista 3.
    print(lista3)

Esercizio1()