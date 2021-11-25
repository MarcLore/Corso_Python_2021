#Scrivi una funzione che dati due numeri in input stampi il numero maggiore
def esercizio1():
    a = input("numero A: ")
    b = input("numero B: ")
    if a > b:
        print("Sono in A > B")
        print(a) 
    elif b > a:
        print("Sono in B > A")
        print(b)
    else:
        print("Sono pari")

esercizio1()




#Scrivi una funzione che dato un numero in input stampi tutti i numeri pari precedenti al numero in input
def esercizio2():
    n = int (input("Inserire numero: "))
    for c in range(0, n):
        if c % 2 == 0:
            print (c)

esercizio2()