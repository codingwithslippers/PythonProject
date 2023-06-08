# Kullanıcıdan alınan basamak sayısı kadar pascal üçgeninin basamaklarını hesaplayan Python kodunu yazınız.


def pascal_ucgeni(basamak_sayisi):
    ucgen = []

    for satir in range(basamak_sayisi):
        satir_listesi = []
        for sira in range(satir + 1):
            if sira == 0 or sira == satir:
                satir_listesi.append(1)
            else:
                deger = ucgen[satir - 1][sira - 1] + ucgen[satir - 1][sira]
                satir_listesi.append(deger)
        ucgen.append(satir_listesi)

    return ucgen

basamak_sayisi = int(input("Pascal üçgeninin kaç basamağını hesaplamak istersiniz? "))

pascal = pascal_ucgeni(basamak_sayisi)

# Pascal üçgenini ekrana yazdırma
for satir in pascal:
    print(' '.join(map(str, satir)).center(50))
