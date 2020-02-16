#esercizio n.18 p.375

consumo = float(input("Quanta acqua hai consumato? "))
print("Hai consumato", consumo, "metri cubi di acqua.")

quotaf = 20

if consumo <= 100:
    prezzo = quotaf + (2.5 * consumo)
elif consumo > 100:
    prezzo = quotaf + (2.5 * 100) + (4 * (consumo - 100))

print("Il costo è di", prezzo, "€")
