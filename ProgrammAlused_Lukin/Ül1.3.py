from math import *
from calendar import c
from datetime import *
from re import A
tana=date.today()
print(f"Täna on {tana}")
# 30/10/2026
tana = tana.strftime("%d/%m/%Y")
print (f"Täna on {tana}")
# Ülesanne 2
print (" ")
print(3 + 8 / (4-2)*4)  
# Sulgudeta ei mõista programm otsuste prioriteeti ja jätkab rangelt kirjutatu järgi.
print(3 + 8 / 4-2*4)  
print(3 + 8 * (4-2)/4)  
print((3 + 8) / (4-2)*4)  
# Ülesanne 3
print (" ")
try:
    r=float(input ("Sisesta ringi raadius  => "))
    a = 2*r
    print ("ruudu külg",round(a,2))
    P = 4*a
    print ("ruudu ümbermõõt",round(P,2))
    S1 = a**2
    print ("ruudu ruut",round(S1,2))
    C = pi * a
    print ("ringi ümbermõõdu pikkus",round(C,2))
    S2 = pi * r**2
    print ("ringi pindala",round(S2,2))
except ValueError:
    print("Viga")
# Ülesanne 4
print (" ")
# ei taha........... väga raske
# Ülesanne 5
print (" ")
print ("kill-koll kill-koll killadi-koll kill-koll killadi-koll kill-koll kill-koll kill-kollkill-koll.".upper())
# Ülesanne 6
print (" ")
print ("Rong see sõitis tsuhh tsuhh tsuhh,")
print ("piilupart oli rongijuht.")
print ("Rattad tegid rat tat taa,")
print ("rat tat taa ja tat tat taa.")
print ("Aga seal rongi peal,")
print ("kas sa tead, kes olid seal?")
print (" ")
print ("Rong see sõitis tuut tuut tuut,")
print ("piilupart oli rongijuht.")
print ("Rattad tegid kill koll koll")
print ("kill koll koll ja kill koll kill.")
# Ülesanne 7
try:
    A = float(input("Esimene arv: "))
    B = float(input("Teine arv: "))
    P = 2*(A+B)
    S = A*B
    print(f"ümbermõõt on {P}")
    print(f"Pind on {S}")
except ValueError:
    print("Viga")
# Ülesanne 8
print (" ")
kütus=int(input("Kui palju kütus te tangitute: ")) 
kilometr=int(input("Kui palju kilometrid te sõidate: ")) 
kulu=(kütus/kilometr)*100
print(f"Keskmine kulu 100 kilometrit on: {kulu}")
# Ülesanne 9
print (" ")
s=29.9/60
vastus= s*1000 
print(vastus)