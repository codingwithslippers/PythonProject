# Kullanıcının satın aldığı benzinin kaç TL tuttuğunu ve bunun ne kadarının vergi olduğunu hesaplayıp ekrana yazdıran programı python kodları ile yazınız. 
# (kullanıcı satın aldığı benzini litre cinsinden girecek - Benzin litre fiyatı: 21,00 TL  - Vergi oranı %86)


litre=int(input("benzin: "))
hesap = litre*21.00
vergi = hesap*0.86
print("vergi:", vergi)
print("vergisiz benzinin fiyatı:", hesap)
print("toplam tutar:", hesap + vergi)