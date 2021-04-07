
#Listenin ilk dört elemanı ile son dört elemanının yerlerini değiştiriyor.
#Question 1
myList = [1,2,3,4,5,6,7,8]
part1=myList[:4]
part2=myList[4:]
myList = part2 + part1
print(myList)

#Girilen "n" sayısına kadar çift sayıları ekrana yazdırıyor.
#Question 2
num = int(input("Dizinin son sayısını giriniz: "))
for i in range(1,num+1):
    if i % 2 == 0:
        print(i)
