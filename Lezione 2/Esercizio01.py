#stampa 10 volte il tuo nome
def esercizio1():
    def stampa_n_volte(nome):
        for i in range(0,10):
            print(nome)

    nome = "Lorenzo"
    stampa_n_volte("Lorenzo")

#esercizio1()


#Stampa un conto alla rovescia
def esercizio2():
    def stampa_n_volte_2(n):
        while n > 0:
            print (n)
            n = n - 1
        print("Via!")

    stampa_n_volte_2(4)

esercizio2()