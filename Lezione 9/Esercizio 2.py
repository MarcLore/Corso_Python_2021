#scrivere un programma Python per creare una lista multidimensionale (liste di liste) con zeri.
def Esercizio01():
    def multidimensional(list_element):
        nums = []
        for i in range(3):
            nums.append([])
            for j in range(list_element):
                nums[i].append(0)
        return nums

    list_element = 5
    print(multidimensional(list_element))

Esercizio01()





#scrivi un programma Python per creare una griglia nxn con numeri.
#es: 3
#[[1, 2, 3], [1, 2, 3], [1, 2, 3]]
def multimensional2():
    lista = []
    n = int(input("Inserisci numero: "))
    for i in range(0,n):                             #per ogni elemento(i) all'interno del range (da 0 ad n(input))
        lista.append([])                             #inserisci n*[] all'interno della lista
        for e in range(0,n):                         #per ogni elemento(e) all'interno del range(da 0, a n+1)
            lista[i].append(e)                       #inserisci nella lista(i) l'elemento e(da 0 ad n)
    print(lista)                           
multimensional2()