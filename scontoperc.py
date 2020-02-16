prezzoprodotto = float(input("Quanto costa il prodotto di cui vuoi calcolare lo sconto?\n"))
sconto = float(input("A quanto ammonta in percentuale lo sconto del prodotto?\n"))

scontop = sconto / 100

scontopp = scontop * prezzoprodotto

prezzof = prezzoprodotto - scontopp

if prezzof.is_integer():
    prezzof = int(prezzof)

print("Il prezzo del prodotto scontato è di "+ str(prezzof) + " euro")