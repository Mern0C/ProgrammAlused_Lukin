from math import *
#Ülesande 2.1
nimi  = input("Sisesta nimi: ")
if nimi.upper()=="JUKU":
    print("lähme Jukuga kinno!")
    if nimi.isupper():
        print ("Ära karju, Juku!")
    elif nimi.islower():
        print("Ära sosista, Juku!")
    try:
        vanus=int(input("Sisesta vanus: "))
        if 0<=vanus < 6:
            pilet="tasutapilet"
        elif 6 <= vanus <= 14:
            pilet="lastepilet"
        elif 14 < vanus < 65:
            pilet="täispilet"
        elif 65<= vanus <=100:
            pilet="sooduspilet"
        else:
            print("viga andmetes")
        try:
            print(f"Juku vanus on {vanus} aastat, seega on vaja osta {pilet}.")
        except NameError:
            print("Piletit ei saa määrata, kuba vanus on vale")
    except ValueError:
        print("Palun sisesta oma vanus numbrina")
else:
    print("Täna kinno ei minna.")

#Ülesande 2.2
pinginaabrid=["Anna", "Vika"]
nimi1  = input("Sisesta esimene  nimi: ")
nimi2  = input("Sisesta teine  nimi: ")
if nimi1.isalpha() and nimi2.isalpha():
    if nimi1.capitalize() in pinginaabrid and nimi2.capitalize() in pinginaabrid:
        print(f"{nimi1} ja {nimi2} on täna pinginaabrid")
    else:
        print(f"{nimi1} ja {nimi2} ei ole täna pinginaabrid")
else:
    print("Viga: nimed peavad koosnema ainult tähtedest")
valik=input("Kas soovid otsida nimede algustähtede järgi? (jah/ei): ").lower()
otsing=False
if valik=="jah":
    algustäht=input("Sisesta algustäht: ").capitalize()
    for nimi in pinginaabrid:
        if nimi.startswith(algustäht):
            print (f"{nimi} algab tähega {algustäht}")
            ootsing=True
    if not otsing:
        print(f"Ühtegi nime, mis algab tähega {algustäht}, ei leitud")

else:
    print("otsingut ei tehta")
#Ülesande 2.3
try:
    a = float(input("Sisesta korteri pikkus: "))
    b = float(input("Sisesta korteri laius: "))
    S = a * b
    print(f"korteri pindala on {S} ruutmeetrit") 
    valik=input("Kas soovid remonti teha? (jah/ei)").lower()
    if valik=="jah":
        try:
            rm_hind=float(input("Sisesta ruutmeetri hind: "))
            hind=round(S*rm_hind,2)
            print(f"põranda vahetamise hind on {hind} eurot")
            valik=input("Kas tahad remonti teha ise? (jah/ei)").lower()
            if valik=="jah":
                print(f"Remonti teeb ise, koguhind on {hind} eurot")
            elif valik=="ei":
                try:
                    töö_hind=float(input("sisesta töö hind ruutmeetri kohta: "))
                    hind=round(hind+S*töö_hind,2)
                    print(f"Remonti teeb professionaal, koguhind on {hind} eurot")
                except:
                    print("Viga: Palun sisesta numbriline väärtus töö hinna jaoks")
            else:
                print("Viga: Palun sisesta jah või ei")
        except:
            print("Viga: Palun sisesta numbriline väärtus ruutmeetri hinna jaoks.")
    else:
        print("Remonti ei tehta.")
except:
    print("Viga: Palun sisesta numbrilised väärtused pikkuse ja laiuse jaoks")
Ülesande 2.4

