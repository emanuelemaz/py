# calcolare radicali

from os import system, name

def clear(): 
   
    if name == 'nt': 
        _ = system('cls') 

print("Scegli l'indice del radicale:")
num1 = int(input(""))
clear()
print("L'indice scelto è", num1)

print("Scegli il radicando del radicale")
num2 = int(input(""))
clear()
print("Il radicando scelto è", num2)

print('Per scegliere un esponente per il radicando premi "1", altrimenti premi "2"')
decisione = int(input(""))
clear()

if decisione == 1:
    print("Digitare l'esponente del radicando")
    esponente = int(input())
    num2 = num2 ** esponente
else:
    esponente = 1

esp = 1/num1
nfin = num2 ** esp

print("Il risultato è", int(round(nfin, 1)))