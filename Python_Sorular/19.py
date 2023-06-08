# Kullanıcın girdiği iki sayı arasındaki sayıların toplamını gösteren Python programini yaziniz.
toplam=0;
sayi1=input('1. Sayı: ')
sayi2=input('2. Sayı: ')
for i in range(int(sayi1)+1,int(sayi2)):
      toplam+=i
print("{0} ile {1} arasındaki sayıların toplamı : {2}".format(sayi1,sayi2,toplam))
 


# Ekran Ciktisi
# 1. Sayı: 5
# 2. Sayı: 9
# 5 ile 9 arasındaki sayıların toplamı : 21