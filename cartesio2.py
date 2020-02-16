from fractions import Fraction as fraz



try:
    x1 = float(input("\nDigita il primo punto: "))
except ValueError:
    print("Input non valido: uscita dal programma.")
    quit()

try:
    y1 = float(input("\nDigita il secondo punto: "))
except ValueError:
    print("Input non valido: uscita dal programma.")
    quit()


if x1.is_integer() and y1.is_integer():
    x1, y1 = int(x1), int(y1)
else:
    x1, y1 = x1, y1


p1 = ("(" + str(x1) + ", " + str(y1) + ")")
print("\np1 = " + str(p1))


try:
    x2 = float(input("\nDigita il primo punto: "))
except ValueError:
    print("Input non valido: uscita dal programma.")
    quit()

try:
    y2 = float(input("\nDigita il secondo punto: "))
except ValueError:
    print("Input non valido: uscita dal programma.")
    quit()


if x2.is_integer() and y2.is_integer():
    x2, y2 = int(x2), int(y2)

else:
    x2, y2 = x2, y2

p2 = ("(" + str(x2) + ", " + str(y2) + ")")

print("\np2 = " + str(p2))

x3, y3 = ((x2) - (x1)) ** 2, ((y2) - (y1)) ** 2

p3 = (x3 + y3) ** 0.5

if float(p3).is_integer():
    print("\nLa distanza fra i due punti è di " + str(int((p3))) + " unità\n")
else:
    print("\nLa distanza fra i due punti è di " + str(p3) + " unità")
    print("\nLa distanza fra i due punti è di " + str(fraz((p3))) + " unità\n")