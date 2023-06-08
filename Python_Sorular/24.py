# Fonksiyon kullanarak genişliği ve yüksekliği girilen dikdörtgenin alanını hesaplayan Python programi yaziniz.
def dikdortgenAlan(genislik, yukseklik):
    alan = float(genislik) * float(yukseklik)
    print ("Alan :",alan)
    return alan
 
gen = input("Genişlik :")
 
yuk = input("Yükseklik : ")
 
dikdortgenAlan(gen, yuk)

# Ekran Ciktisi
# Genişlik :15
# Yükseklik : 25
# Alan : 375.0