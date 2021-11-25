#moltiplica i numeri precedenti dati da input
#es: 4
#1 * 1 = 1, 1 * 2 = 2, 2 * 3 = 6, 6 * 4 = 24
def moltiplicazionenumeri():
    prodottototale = 1
    numerodamoltiplicare = int(input("Inserisci un numero: "))

    for i in range(1, numerodamoltiplicare + 1):
        prodottototale = prodottototale * i

        print ("la moltiplicazione totale è: ", prodottototale)

#moltiplicazionenumeri()




#Scrivi una funzione che stampi la tabellina del 2
def moltiplicazionedel2():
    n = 2
    for i in range (1, 10 + 1):
        product = n * i
        print (product)

moltiplicazionedel2()