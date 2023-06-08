# Girilen Sayının Asal Sayı mı Değil mi olduğunu bulan Python python programini yaziniz.
sayac=0
sayi=input('Sayı: ')
for i in range(2,int(sayi)):
      if(int(sayi)%i==0):
            sayac+=1
            break
if(sayac!=0):
      print("Sayı Asal Değil")
else:
      print("Sayı Asal")


# Ekran Ciktisi
# Sayı: 15
# Sayı Asal Değil