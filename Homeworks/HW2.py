#Girilen kullanıcı adı ve parola bilgisini sistemte kayıtlı olan kullanıcı adı ve parola ile karşılaştırıyor.
#Sağlanan koşula göre kullanıcı adı / parola / kullanıcı ado - parola hatalı çıktısını üretiyor. 
#Bunların dışındaki durumda kullanıcı adı ve parola doğru olacağından giriş başarılı çıktısı üretiliyor..

#Question 1
sysUserName = "user"
sysPassword = "python"

userName = input("Kullanıcı Adı: ")
password = input("Parola: ")

if sysUserName != userName and sysPassword != password:
    print("Giriş başarısız. \nKullanıcı adı ve parola hatalı.")
elif sysUserName == userName and sysPassword != password:
    print("Giriş başarısız. \nParola hatalı")
elif sysUserName != userName and sysPassword == password:
    print("Giriş başarısız. \nKullanıcı adı hatalı.")
else:
    print("Giriş başarlı.")

#Alternatif Çözüm
userInfo ={"sysUserName":"user","sysPassword":"python"}
userName = input("Kullanıcı Adı: ")
password = input("Parola: ")

if userInfo["sysUserName"] != userName and userInfo["sysPassword"] != password:
    print("Giriş başarısız. \nKullanıcı adı ve parola hatalı.")
elif userInfo["sysUserName"] == userName and userInfo["sysPassword"] != password:
    print("Giriş başarısız. \nParola hatalı")
elif userInfo["sysUserName"] != userName and userInfo["sysPassword"] == password:
    print("Giriş başarısız. \nKullanıcı adı hatalı.")
else:
    print("Giriş başarlı.")
