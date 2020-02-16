from math import pi as pigreco
r = int(input("\n Digita il raggio del cerchio di cui vuoi area e circonferenza: "))

print("Scegli fra le unità di misura \n1: metri \n2: decimetri \n3: centimetri \n4: millimetri")
scelta1 = int(input())
if scelta1 == 1:
    um = "m"
elif scelta1 == 2:
    um = "dm"
elif scelta1 == 3:
    um = "cm"
elif scelta1 == 4:
    um = "mm"

area = pigreco * r ** 2
areapi = (str(r ** 2) + "π")
circ = pigreco * r * 2
circpi = (str(r * 2) + "π")

print("L'area del cerchio è di:", areapi, "≃",  str(area), um + "²")
print("La circonferenza del cerchio è di:", circpi, "≃", str(circ), um)