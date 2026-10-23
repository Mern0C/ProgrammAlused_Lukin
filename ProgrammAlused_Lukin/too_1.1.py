print("Tere,maailm")
nimi = input ( "Sisesta oma nimi: " )
print(f"Tervitan sind,{nimi}")
try:
    vanus=int(input("Sisesta oma vanus: "))
    print (f"Sa oled {vanus} aastat vana.")
except ValueError:
    print("palun, sisesta kehtiv number vanuse jaoks")