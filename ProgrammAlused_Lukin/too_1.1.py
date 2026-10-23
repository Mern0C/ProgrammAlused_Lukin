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
try:
    kommid=int(input("Mitu kommi soovid ära võtta? "))
    kommide_arv -= kommid
    print(f"Laud on nüüd {kommide_arv} kommi")
except ValueError:
    print("Palun sisesta number")
#Ülesanne 4
print (" ")
try:
    ümbermõõt=float(input("Sisesta puu ümbermõtt: "))
    läbimõõt=round(ümbermõõt/pi,1)
    print (f"Puu läbimõõt on: {läbimõõt}")
except ValueError:
    print("Palun sisesta number")
#Ülesanne 5
print (" ")
try:
    N=float(input("Sisesta ristküliku esimene külg (N)"))
    M=float(input("Sisesta ristküliku teine külg (M)"))
    diagonaal=round(sqrt(N**2 + M**2), 1)
    print(f"Ristküliku diagonaal on {diagonaal}")
except ValueError:
    print("Palun sisesta number")
#Ülesanne 6
print (" ")
try:
    aeg = float(input("Mitu tundi kulus sõiduks? "))
    teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
    kiirus = teepikkus / aeg
    print("Sinu kiirus oli " + str(kiirus) + " km/h")
except ValueError:
    print("Palun sisesta number")
#Ülesanne 7
print (" ")
try:
    arv1=int(input("esimene arv: "))
    arv2=int(input("teine arv: "))
    arv3=int(input("kolmas arv: "))
    arv4=int(input("neljas arv: "))
    arv5=int(input("viies arv: "))
    summa=arv1+arv2+arv3+arv4+arv5
    keskmine=summa/5
    print(f"Summa: {summa}, Keskmine: {keskmine}")
    jagaja=int(input("sisesta arv, millega jagada: "))
    tulemus=summa/jagaja
    print("Tulemus: ", tulemus)
    print("täisarvuline osa: ", int(tulemus))
    print("Jääk: ", summa % jagaja)
except ValueError:
    print("Palun sisesta number")


