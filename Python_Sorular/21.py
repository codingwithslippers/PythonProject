# 1 den kullanıcının girmiş olduğu sayıya kadar olan tek ve çift sayıların toplamını ayrı ayrı bulan ve sonucu ekranda gösteren Python programini yaziniz.
sayi = input('Sayıyı Girin : ')
tekToplam=0
ciftToplam=0
for i in range(1,int(sayi)):
      if(i%2==0):
            ciftToplam+=i
      else:
            tekToplam+=i
print("Tek Sayıların Toplamı : {0}".format(tekToplam))
print("Çift Sayıların Toplamı : {0}".format(ciftToplam))

# Ekran Ciktisi
# Sayıyı Girin : 5 
# Tek Sayıların Toplamı : 4
# Çift Sayıların Toplamı : 6