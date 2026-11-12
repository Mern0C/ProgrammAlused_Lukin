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

