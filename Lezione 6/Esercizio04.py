#Funzione che restituisce True o Flase, se la stringa ha un numero di caratteri che è un multiplo di 4
def is_multiplodi4():

    s = input("inserisci: ")

    contatore = 0
    
    for carattere in s:
        contatore = contatore + 1        

    if (contatore % 4 == 0):
        print(True)
    else:
        print(False)

is_multiplodi4()