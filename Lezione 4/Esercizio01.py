#Scrivi una funzione che stampi il numero di lettere di una data stringa con il ciclo for
def Esercizio2ConFor():
    s = input ("inserisci stringa: ")
    lunghezza_stringa = 0
    for i in range (0, len(s)):
        lunghezza_stringa = lunghezza_stringa + 1
    print(lunghezza_stringa)

#Esercizio2ConFor()


#Scrivi una funzione che stampi il numero di lettere di una data stringa con il ciclo while
def Esercizio2ConWhile():
    s = input ("inserisci stringa: ")
    contatore = 0
    lunghezza_stringa = 0
    while contatore < len(s):
        lunghezza_stringa = lunghezza_stringa + 1
        contatore = contatore + 1
    print(lunghezza_stringa)
    
#Esercizio2ConWhile()






#Scrivi una funzione che stampi le ultime due lettere di una data stringa x4 volte
def esercizio3():
    s = input ("inserisci stringa: ")
    while len(s) < 2:
        s = input("inserisci stringa piu lunga: ")
    ns = s[-2] + s[-1]
    for i in range (0, 3):
        ns = ns + s[-2] + s[-1]
    print(ns)

#esercizio3()




#Scrivi una funzione che data una stringa in input restituisca la stringa stampata in maiuscolo e minuscolo
def esercizio4():
    s = input ("inserisci stringa: ")
    print(s.upper())
    print(s.lower())

#esercizio4()




#Scrivi una funzione che data una stringa la ristampa in maiuscolo i caratteri dispari e in minuscolo i caratteri pari
def esercizio6():
    s = input ("inserisci stringa: ")
    contatore = 0

    while(contatore < len(s)):
        c = s[contatore]

        if(contatore % 2 == 0):
            print(c.upper())

        else:
            print(c.lower())

        contatore = contatore + 1

esercizio6()