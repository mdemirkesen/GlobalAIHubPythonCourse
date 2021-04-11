soru1 = "Güneşe en yakın gezegen hangisidir?"
soru2 = "Periyodik cetvelde 'Fe' ile gösterilen element adı nedir? "
soru3 = "Malatya ilimizin plaka kodu nedir?"
soru4 = "Python dosyalarının uzantısı nedir?"
soru5 = "EURO 2021 hangi ülkede düzenlenecektir?"
cevap1, cevap2, cevap3, cevap4, cevap5 = "merkür","demir","44","py","italya"
soru6 = "Göbeklitepe hangi ilimizdedir?" 
soru7 = "Roger Federer hangi spor dalında şampiyonluklar elde etmiştir?"
soru8 = "Elon Musk'ın sahibi olduğu uzay taşımacılığı şirketinin adı nedir"
soru9 = "'OD' hangi yazarımıza ait bir romandır"
soru10= "'Dağlar Dağlar','Gülpembe','Kol Düğmeleri' gibi şarkılarıyla ünlü sanatçımız kimdir? "
cevap6, cevap7, cevap8, cevap9, cevap10 ="şanlıurfa","tenis","spacex","iskender pala","barış manço"

yarisma = {soru1:cevap1, soru2:cevap2, soru3:cevap3, soru4:cevap4, soru5:cevap5,
           soru6:cevap6, soru7:cevap7, soru8:cevap8, soru9:cevap9, soru10:cevap10}
puan=0
soruNo=0
for soru in yarisma:
    soruNo+=1
    print("Soru - {}: {}".format(soruNo,soru))
    cevap=input("Yanıtnız: ")
    cevap=cevap.replace("I","ı").replace("İ","i")
    if cevap.lower() == yarisma[soru]:
        print("Doğru")
        puan+=10
    else:
        print("Yanlış")

print("{} soruya doğru cevap verdiniz. Toplam puanınız: {}".format(int(puan/10),puan))
if puan>=60:
    print("Tebrikler, başarılı oldunuz.")
else:
    print("Malesef başarılı olamadınız.")
