#Scrivi un programma Python per estrarre un dato numero di elmenenti 
#(preso in input) selezionati casualmente da una data lista.

#SOLUZIONE1
def esercizio1():
    import random
    lista = [1, "g", "ciao", 32, "w"]
    n = int(input("Inserisci numero di elementi da restituire: "))

    contatore = 0
    while (contatore < n):
        print(random.choice(lista))
        contatore = contatore + 1

#esercizio1()




#SOLUZIONE2
def soluzione2():
    import random
    def random_select_nums(n_list, n):                     #definire nome della funzione.
        return random.sample(n_list, n)                    #random_select_nums richiama(return) la funzione random.sample.
                                                           #.sample è un metodo che permette di generare casualmente degli elementi in una lista, tupla o stringa.

    n_list = [1,1,2,3,4,4,5,1]                             #lista.
    selec_nums = 5                                         #numero di elementi da prendere in lista.
    result = random_select_nums(n_list, selec_nums)        #usa la funzione (random_select_nums), generata inizialmente.
    print(result)                                          #stampa gli elementi.

#soluzione2()




#SOLUZIONE3
def soluzione3():
    def random_select_nums_with_randint(n_list, n):
        import random
        for i in range(0,n):
            random_number = random.randint(0, len(n_list)-1)

            print(random_number)
            print(n_list[random_number])

    n_list = ["a", "a", "b", "f", "h", "k", "t", "t"]
    selec_nums = 3
    random_select_nums_with_randint(n_list, selec_nums)

soluzione3()