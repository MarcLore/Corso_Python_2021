#Funzione che dato un numero lo ristampa ma con un numero di zeri tanti quanti erano i numeri della stringa
def es5():
    num = input("Inserisci numero: ")
    numero_di_zeri = ""
    numeri_in_stringa = num

    for i in range (0, len(numeri_in_stringa)):
        numero_di_zeri = numero_di_zeri + "0"
    print(numero_di_zeri + numeri_in_stringa)
       
es5()