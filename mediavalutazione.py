def inflo(a):
    a = float(a)
    if a.is_integer():
        a = int(a)
    else:
        a = a
def mean(a):
    return sum(a) / len(a)

voti = []

v1 = float(input("\nInserisci il primo voto: "))
voti.append(v1)
print("\nHai digitato", ((voti[0])))
while True:
        v2 = float(input("\nDigita il voto successivo: "))
        voti.append(v2)
        media = voti
        medvo = mean(voti)
        if medvo.is_integer() == True:
            medvo = int(medvo)
        else:
            medvo = medvo
        print("\nLa media attuale è", str(medvo))
        f = input("\nVuoi aggiungere un altro voto? (s/n)")
        if f == "n":
            media = mean(voti)
            if media.is_integer() == False:
                d = input("\nVuoi arrotondare la media (s/n)? ")
                if d == "s":
                    media = float(round(media, 1))
                    media = float(round(media, 0))
                    print("\nIl voto finale è", int(media))
                elif d == "n":
                    media = float(media)
                    print("\nIl voto finale è", media)
                if media < 4.5:
                    giudizio = "gravemente insufficiente"
                    print("\nIl giudizio è", giudizio)
                elif 4.5 <= media < 6:
                    giudizio = "insufficiente"
                    print("\nIl giudizio è", giudizio)
                elif 6 <= media < 7.5:
                    giudizio = "sufficiente"
                    print("\nIl giudizio è", giudizio)
                elif 7.5 <= media < 9:
                    giudizio = "buono"
                    print("\nIl giudizio è", giudizio)
                elif media >= 9:
                    giudizio = "eccellente"
                    print("\nIl giudizio è", giudizio)
                print("\n")
                quit()
            else:
                media = float(media)
                print("\nIl voto finale è", int(media))
                if media < 4.5:
                    giudizio = "gravemente insufficiente"
                    print("\nIl giudizio è", giudizio)
                elif 4.5 <= media < 6:
                    giudizio = "insufficiente"
                    print("\nIl giudizio è", giudizio)
                elif 6 <= media < 7.5:
                    giudizio = "sufficiente"
                    print("\nIl giudizio è", giudizio)
                elif 7.5 <= media < 9:
                    giudizio = "buono"
                    print("\nIl giudizio è", giudizio)
                elif media >= 9:
                    giudizio = "eccellente"
                    print("\nIl giudizio è", giudizio)
                print("\n")
                quit()
