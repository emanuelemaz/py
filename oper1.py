print('Inserire due valori x e y: il programma calcolerà (x+y)/(x-y)')

x = input("\nDigita il valore x: ")

y = input("\nDigita il valore y: ")

v = (float(x) + float(y)) / (float(x) - (float(y)))
print("\n")
print("Il risultato è:", v)
print("\n")
print("(" + str(x) + "+" + str(y) + ")" + "/" + "(" + str(x) + "-" + str(y) + ")" + "=" + str(v))