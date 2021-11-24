#scrivere un programma Python per aggiungere un elemento preso in input in una tupla.
def Esercizio_Tupla01():
    t = ("a", "b", "c")
    s = input("Inserire stringa da inserire in tupla: ")
    t2 = t + (s,)
    print(t2)

Esercizio_Tupla01()