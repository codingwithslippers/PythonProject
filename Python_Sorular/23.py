# Fonksiyon kullanarak yarıçapı girilen dairenin alanını hesaplayan Python programini yaziniz.
def daireAlan(yaricap):
    alan = float(yaricap) * float(yaricap)*3.14
    print ("Alan :",alan)
    return alan
 
r = input("Yarıçapı Gir :")
 
daireAlan(r)


# Ekran Ciktisi
# Yarıçapı Gir :3
# Alan : 28.26