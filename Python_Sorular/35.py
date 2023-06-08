# Bir sayının kendisi dışında bütün pozitif bölenlerinin toplamı kendisine eşit olan sayılara mükemmel sayı denir. Kullanıcıdan alınan sayının mükemmel sayı olup olmadığını kontrol eden Python kodunu yazınız.


sayi = int(input("Sayi Giriniz:"))

toplam=0

for i in range(1,sayi):
    print(i)
    if(sayi%i == 0):
        toplam +=i
        
if(sayi == toplam):
    print("Mükemmel Sayidir.")
else:
    print("Mükemmel Sayi Degildir")