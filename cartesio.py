from fractions import Fraction as risfraz

x1 = input("\n Digita il punto x1: ")
y1 = input("\n Digita il punto y1: ")
p1 = str((" (" + x1 + ", " + y1 + ")"))
print("\n" + str(p1))
x2 = input("\n Digita il punto x2: ")
y2 = input("\n Digita il punto y2: ")
p2 = str((" (" + x2 + ", " + y2 + ")"))
print("\n" + str(p2))

x3, y3 = (int(x2) - int(x1)) ** 2, (int(y2) - int(y1)) ** 2

p3fl = (float(x3 + y3) ** float(0.5))
p3fr = risfraz(float(x3 + y3) ** float(0.5))

if p3fl.is_integer() == False:
    print("\n", "La distanza è di circa", p3fr, "unità")
    print("\n", "La distanza è di circa", p3fl, "unità ")


elif p3fl.is_integer():
    p3fl = int(p3fl)
    print("\n", "La distanza è di", p3fl, "unità ")