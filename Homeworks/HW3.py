#Explain your work

#Question 1

karne={}
bilgiler={}
notlar=[]

for i in range(5):
    print(i+1,". ",end="")
    isim=input("Öğrencinin Adı: ")
    araSinav=int(input("Ara sınav notu: "))
    proje=int(input("Proje notu: "))
    final=int(input("Final notu: "))
    ort = araSinav*0.3+proje*0.3+final*0.4
    notlar.append(ort) 
    bilgiler["Ara Sınav"]=araSinav
    bilgiler["Proje"]=proje
    bilgiler["Final"]=final
    karne[isim]=bilgiler
    bilgiler={}

# Öğrenci bilgilerinin yazdırılması
for i in karne:
    print(i,end=" ")
    for j in karne[i]:
        print(j,karne[i][j],end=" ")
    print()

print(notlar) # Notların işlem görmeden  giriş sırasına göre yazdırılması.

yuksekNot = max(notlar)
highest = notlar.index(yuksekNot)
tempMax = notlar[highest]
notlar.pop(highest)
notlar.insert(0,tempMax)


dusukNot = min(notlar)
lowest = notlar.index(dusukNot)
tempMin = notlar[lowest]
notlar.pop(lowest)
notlar.append(tempMin)


print(notlar) # Notların işlem gördükten sonra yazdırılması
