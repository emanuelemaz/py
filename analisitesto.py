#i = numero indice della lettera
#lettera = nome della lettera

s = input("Inserisci la stringa da analizzare per lettere: ")

for i, lettera in enumerate(s):
    print("Lettera: " + str(lettera) + " Posizione: " + str(i + 1))