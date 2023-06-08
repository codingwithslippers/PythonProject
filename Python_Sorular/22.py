# Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteren Python programi ornegini giriniz.
yeniMaas=0
maas=input("Maaşı Gir : ")
zam=input("Zam Oranı(%) : ")
yeniMaas=int(maas)+(int(maas)*int(zam)/100)
print("Zamlı Maaş :",yeniMaas)


# Ekran Ciktisi
# Maaşı Gir : 8500
# Zam Oranı(%) : 30
# Zamlı Maaş : 11050.0