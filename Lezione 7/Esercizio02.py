#Scrivi un programma Python per trovare l'elenco di parole più lunghe di n da 
#un determinato elenco di parole. Parametro n e lista di parole passato in input.
def Esercizio2():
    Lista_parole = []
    lista_result = []

    contatore = 0
    while contatore < 5:
        if contatore < 4:
            lista = input("Inserisci parola: ")
            contatore = contatore + 1
            Lista_parole.append(lista)

        else:
            n = int(input("Inserisci numero: "))
            contatore = contatore + 1

    for parola in Lista_parole:
        if len(parola) > n:
            lista_result.append(parola)

    print(lista_result)

Esercizio2()