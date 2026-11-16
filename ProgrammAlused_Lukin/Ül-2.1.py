from math import *
from random import *
# #Ülesande 2.1
# nimi  = input("Sisesta nimi: ")
# if nimi.upper()=="JUKU":
#     print("lähme Jukuga kinno!")
#     if nimi.isupper():
#         print ("Ära karju, Juku!")
#     elif nimi.islower():
#         print("Ära sosista, Juku!")
#     try:
#         vanus=int(input("Sisesta vanus: "))
#         if 0<=vanus < 6:
#             pilet="tasutapilet"
#         elif 6 <= vanus <= 14:
#             pilet="lastepilet"
#         elif 14 < vanus < 65:
#             pilet="täispilet"
#         elif 65<= vanus <=100:
#             pilet="sooduspilet"
#         else:
#             print("viga andmetes")
#         try:
#             print(f"Juku vanus on {vanus} aastat, seega on vaja osta {pilet}.")
#         except NameError:
#             print("Piletit ei saa määrata, kuba vanus on vale")
#     except ValueError:
#         print("Palun sisesta oma vanus numbrina")
# else:
#     print("Täna kinno ei minna.")

# #Ülesande 2.2
# pinginaabrid=["Anna", "Vika"]
# nimi1  = input("Sisesta esimene  nimi: ")
# nimi2  = input("Sisesta teine  nimi: ")
# if nimi1.isalpha() and nimi2.isalpha():
#     if nimi1.capitalize() in pinginaabrid and nimi2.capitalize() in pinginaabrid:
#         print(f"{nimi1} ja {nimi2} on täna pinginaabrid")
#     else:
#         print(f"{nimi1} ja {nimi2} ei ole täna pinginaabrid")
# else:
#     print("Viga: nimed peavad koosnema ainult tähtedest")
# valik=input("Kas soovid otsida nimede algustähtede järgi? (jah/ei): ").lower()
# otsing=False
# if valik=="jah":
#     algustäht=input("Sisesta algustäht: ").capitalize()
#     for nimi in pinginaabrid:
#         if nimi.startswith(algustäht):
#             print (f"{nimi} algab tähega {algustäht}")
#             ootsing=True
#     if not otsing:
#         print(f"Ühtegi nime, mis algab tähega {algustäht}, ei leitud")

# else:
#     print("otsingut ei tehta")
# #Ülesande 2.3
# try:
#     a = float(input("Sisesta korteri pikkus: "))
#     b = float(input("Sisesta korteri laius: "))
#     S = a * b
#     print(f"korteri pindala on {S} ruutmeetrit") 
#     valik=input("Kas soovid remonti teha? (jah/ei)").lower()
#     if valik=="jah":
#         try:
#             rm_hind=float(input("Sisesta ruutmeetri hind: "))
#             hind=round(S*rm_hind,2)
#             print(f"põranda vahetamise hind on {hind} eurot")
#             valik=input("Kas tahad remonti teha ise? (jah/ei)").lower()
#             if valik=="jah":
#                 print(f"Remonti teeb ise, koguhind on {hind} eurot")
#             elif valik=="ei":
#                 try:
#                     töö_hind=float(input("sisesta töö hind ruutmeetri kohta: "))
#                     hind=round(hind+S*töö_hind,2)
#                     print(f"Remonti teeb professionaal, koguhind on {hind} eurot")
#                 except:
#                     print("Viga: Palun sisesta numbriline väärtus töö hinna jaoks")
#             else:
#                 print("Viga: Palun sisesta jah või ei")
#         except:
#             print("Viga: Palun sisesta numbriline väärtus ruutmeetri hinna jaoks.")
#     else:
#         print("Remonti ei tehta.")
# except:
#     print("Viga: Palun sisesta numbrilised väärtused pikkuse ja laiuse jaoks")
# # Ülesande 2.4
# try:
#     summa = float(input("Ostusumma: "))
#     if summa > 700:
#         print("Allahindlus 30%")
#         soodushind=round(summa*0.7 ,2)
#         print(f"kogushind on {soodushind} eurot") 
#     else:
#         print("Allahindlust pole")
# except ValueError:
#     print("Viga: Palun sisesta numbrid")
# # Ülesande 2.5
# try:
#     temperatuur=float(input("Milline on toa temperatuur?: "))
#     if 26 > temperatuur >= 18:
#         print("Talvel on see soovitatav toatemperatuur")
#     else:
#         print("see on ebasoovitav temperatuur")
# except ValueError:
#     print("Viga: Palun sisesta numbrid")
# # Ülesande 2.6
# # 160 ja alla selle = väike
# # 161 kuni 180 = keskmine
# # 180 ja üle selle = pikk 
# try:
#     pikkus=float(input("märkige oma pikkus: "))
#     if 160 >= pikkus > 50:
#         print("Teie pikkus on lühike")
#     elif 160 < pikkus < 180:
#         print("Teie pikkus on keskmine")
#     elif pikkus >= 180 > 270:
#         print("Teie pikkus on pikk")
#     else:
#         print("ära valeta")
# except ValueError:
#     print("Viga: Palun sisesta numbrid")
# # Ülesande 2.7
# # Ülesande 2.8
# summa=0
# arve="Toode Kogus Hind  Kokku\n"
# valik=input ("kas soovid osta piima? (jah/ei): ")
# if valik.lower()=="jah":
#         kogus=int(kogus)
#         piim_hind=round(uniform(0.5, 3), 2)
#         print(f"Piima hind on {piim_hind} eurot.")
#         summa+=kogus*piim_hind
#         print(f"Piima kogusumma on {kogus*piim_hind} eurot.")
#         arve+=f"piim   {kogus}   {piim_hind}€    {kogus*piim_hind}€\n"
# else:
#     print("Selge: Piima ei taha")
# print(f"Kogusumma on:{round(summa,2)} eurot.")

# valik=input("Kas soovid osta sai? (jah/ei): ")
# if valik.lower()=="jah":
#     kogus=input("Kui palju sai soovid osta (täisarv): ")
#     if kogus.isdigit():
#         kogus=int(kogus)
#         sai_hind=round(uniform(0.5, 3), 2)
#         print(f"Sai hind on {sai_hind} eurot.")
#         summa+=kogus*sai_hind
#         print(f"Sai kogusumma on {round(kogus*sai_hind,2)} eurot.")
#         arve+=f"sai   {kogus}   {round(sai_hind,2)}€    {round(kogus*sai_hind,2)}€\n"
# print(f"Kogusumma on:{round(summa,2)} eurot.")
# valik=input("Kas soovid osta leiba? (jah/ei): ")
# if valik.lower()=="jah":
#      kogus=input("Kui palju leiba soovid osta (täisarv): ")
#      if kogus.isdigit():
#         kogus=int(kogus)
#         leib_hind=round(uniform(0.5, 3), 2)
#         print(f"Leiva hind on {round(leib_hind,2)} eurot.")
#         summa+=kogus*leib_hind
#         print(f"Leiva kogusumma on {round(kogus*leib_hind,2)} eurot.")
#         arve+=f"leib   {kogus}   {round(leib_hind,2)}€    {round(kogus*leib_hind,2)}€\n"
# print(f"Kogusumma on:{round(summa,2)} eurot.")
# # Lõpus kuva tšekk: iga ostetud toote nimi, kogus, hind ja summa ning kõige all kogusumma.
# print("Arve NR: 0000")
# print("--------------")
# print(arve)
# Ülesande 2.9
try:
    a = float(input("Sisesta 1.arv: "))
    b = float(input("Sisesta 2.arv: "))
    c = float(input("Sisesta 3.arv: "))
    d = float(input("Sisesta 4.arv: "))
    if a>0 and b>0 and c>0 and d>0:
        if a==b==c==d:
            print("See on ruut")
        else:
            print("see on nelinurk")
    else:
         print("Palun sisesta positiivsed arvud.")
except:
    print("Viga: Palun sisesta numbrili")