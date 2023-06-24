# Verilen bir liste üzerindeki çift sayıları filtreleyen bir Python fonksiyonu nasıl yazılır?


def cift_sayilari_filtrele(liste):
    ciftler = [sayi for sayi in liste if sayi % 2 == 0]
    return ciftler

# Örnek kullanım
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(cift_sayilari_filtrele(liste))
