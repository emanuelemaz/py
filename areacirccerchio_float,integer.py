from math import pi as pigreco
r = (float(input("\nDigita il raggio del cerchio di cui vuoi area e circonferenza: ")))

if r.is_integer():
    r = int(r)
else:
    r = float(r)

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

area_approssimata = pigreco * r ** 2
area_inpigreco = (str(r ** 2) + "π")
circ_approssimata = pigreco * r * 2
circ_inpigreco = (str(r * 2) + "π")

print("L'area del cerchio è di:", area_inpigreco, "≃",  str(area_approssimata), um + "²")
print("La circonferenza del cerchio è di:", circ_inpigreco, "≃", str(circ_approssimata), um)