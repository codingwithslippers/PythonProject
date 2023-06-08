# Öğrencilerine 12 haneli öğrenci numarası veren üniversitenin verdiği numaranın ilk 4 hanesi giriş yılı 5. ve 6.  hanesi okuduğu fakültenin numarası 7. ve 8. hane bölüm numarası 9. hanesi öğrenim numarası 11. ve 12. hane ise öğrencinin üniversiteye giriş sırasıdır. 12 haneli öğrenci kodunu kullanıcıdan alarak anlamlı şekilde ayıran kodu yazınız.

#Baska Bir Kod - Python Soru / Cevap 

okul_numarasi = input("Okul numaranızı giriniz: ")
no = str(okul_numarasi)

d1 = {
    "GirisYili": no[:4],
    "FokulteNo": no[4:6],
    "BolumNo": no[6:8],
    "OgrenimNo": no[8:9],
    "Ogrenci Giriş Sırası": no[10:12]
}

print("NUMARANIN ACILIMI:")

for k, v in d1.items():
    print(k + ": " + v)
