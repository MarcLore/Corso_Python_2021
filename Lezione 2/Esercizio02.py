#somma i numeri precedenti a quello dato in input
def stampasommatoria():
    numero = int(input("inserisci numero da sommare "))
    risultato = 0

    for i in range (1, numero+1):
        risultato = risultato + i

    print(risultato)

stampasommatoria()