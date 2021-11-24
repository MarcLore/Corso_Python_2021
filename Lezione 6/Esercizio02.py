#Funzione che data una stringa, stampa i singoli caratteri alternandoli tra maiuscole e minuscole
def esercizio3():
    s = input ("inserisci stringa: ")
    contatore = 0

    while(contatore < len(s)):
        c = s[contatore]

        if(contatore % 2 == 0):
            print(c.upper())

        else:
            print(c.lower())

        contatore = contatore + 1

esercizio3()