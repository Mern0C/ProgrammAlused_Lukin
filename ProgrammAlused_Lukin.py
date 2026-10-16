print ("Hello, World!")
print ("Tere tulemast \t!")
print ("Õpin",1,".kursusel") #sep=" " vaikimisi on tühik
print ("Õpin",1,".kursusel",sep="¤")
print (" ")
print("2026", "10", "01", sep="-")
print("Sama ", end="") #end "\n" tahendab enter
print("rida")


nimi = "Python" #str ehk sõne
print ("Tere,", nimi)
kursus=1
print ("Õpin",kursus,".kursusel")

print (" ")
nimi = input ("Sisesta oma nimi: ")  #vastus
print ("Tere,", nimi)
kursus=int(input ("Sisesta kursuse number: "))
print ("Õpin",kursus,".kursusel")
print ("Järgmisel aastan õpin",kursus+1, ".kursusel") #kursus+1 suurendeb 1 võrra

a =float(input("Esimene arv: "))
b =float(input("Teine arv: "))
print(a,"+",b, "=", a + b) 
a =float(input("Esimene arv: "))
b =float(input("Teine arv: "))
print(a,"-",b, "=", a - b) 
a =float(input("Esimene arv: "))
b =float(input("Teine arv: "))
print(a,"**",b, "=", a ** b) 
a =float(input("Esimene arv: "))
b =float(input("Teine arv: "))
print(a,"*",b, "*", a + b)
a =float(input("Esimene arv: "))
b =float(input("Teine arv: "))
print("(", a,"+",b, ")", "/", 2, "=", (a + b)/2) 
print("Ümardatud arv: ", round((a + b)/2,2 ))
print (" ")
a =float(input("Esimene arv: "))
tehe =input("Tehe: ")
b =float(input("Teine arv: "))
print(f"{a} {tehe} {b} = {eval(f'{a} {tehe} {b}')}")
print (" ")
nimi = "Mari"
punktid = 87
print(f"{nimi} sai {punktid} punkti.")
