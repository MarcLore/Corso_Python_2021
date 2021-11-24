
def esercizio4():
    s = input ("inserisci stringa: ")
    contatore = 0
    result = ""

    while(contatore < len(s)):
        c = s[contatore]

        if(contatore % 2 == 0):
            result = result + c.upper()

        else:
            result = result + c.lower()

        contatore = contatore + 1
        print(result)

esercizio4()