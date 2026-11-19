try:
    print("1 - Arvu kontroll")
    print("2 - Kehamassiindeks")
    print("3 - Ostu allahindlus")
    programm=int(input("Vali programm: "))
    if programm==1:
        print("Arvu kontroll") #' -> "
        arv=float(input("Sisesta täisarv => ")) ##lisasin float()
        if arv>0: #lisasin :
            print("Arv on positiivne")
        elif arv==0: # = -> ==
            print("Arv on null")
        else:
            print("Arv on negatiivne") #lisasin tab
        if arv%2==0:
            print("Arv on paarisarv")
        else:
            print("Arv on paaritu")
        if arv/3: 
            print("Arv jagub 3-ga")
        else:
            print("arv ei jaguv 3-ga")
        print("Kehamassiindeks")
    elif programm==2:
        mass=float(input("Sisesta kaal (kg) => "))
        pikkus=float(input("Sisesta pikkus (m) => ")) #lisasin )
        if pikkus or mass<= 0:
            print("see ei sobib")
        else:
            kmi=mass/pikkus*2
            print("KMI:", round(kmi,1))
            if kmi<18.5:
                print("Alakaal")
            elif kmi>=18.5:
                print("Normaalkaal")
            elif kmi>=25: 
                print("Ülekaal")
            elif kmi>=30: #lisasin :
                print("Rasvumine")
            print()
            print("Ostu allahindlus")
    elif programm==3:
        summa=float(input("Sisesta ostusumma => "))
        if summa<=0: #"=<" -> ">="
            print("Vigane summa")
        elif summa>500:
            print("Allahindlus 10%, maksta:", round(summa*0.9,2)) #kohade vahetus 5% ridast 10%ridasse 
        elif summa>100 or summa<=500:
            print("Allahindlus 5%, maksta:", round(summa*0.95,2))
        else: #lisasin :
            print("Allahindlust pole, maksta:", summa) #lisasin )
    else:
        print("Vigane valik")
except ValueError:
    print("palun sisesta arv") ##lisasin try: ja except:
except ZeroDivisionError:
    print("nulliga jagada ei saa")

