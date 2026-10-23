from random import *
from math import *
#ülesanne 1
print("Tere,maailm")
nimi = input ( "Sisesta oma nimi: " )
print(f"Tervitan sind,{nimi}")
try:
    vanus=int(input("Sisesta oma vanus: "))
    print (f"Sa oled {vanus} aastat vana.")
except ValueError:
    print("palun, sisesta kehtiv number vanuse jaoks")
#ülesanne 2
print (" ")
vanus =18
eesnimi="Jaak"
pikkus=16.5
kas_käib_koolis=True
print (f"Vanus: {vanus}, tüüp: {type(vanus)}")
print (f"eesnim: {eesnimi}, tüüp: {type(eesnimi)}")
print (f"pikkus: {pikkus}, tüüp: {type(pikkus)}")
print (f"Käib koolis: {kas_käib_koolis}, tüüp: {type(kas_käib_koolis)}")
#Ülesanne 3
print (" ")
#kommide_arv=int(input("Kommide arv: "))
kommide_arv=randint(1, 100)
print(f"Laud on {kommide_arv} kommi")
kommid=int(input("Mitu kommi soovid ära võtta? "))
kommide_arv -= kommid
print(f"Laud on nüüd {kommide_arv} kommi")
