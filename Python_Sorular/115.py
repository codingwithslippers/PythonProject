# Verilen bir sayı listesindeki tek sayıların karelerini ve çift sayıların küplerini hesaplayan bir Python fonksiyonu nasıl yazılır?

def kare_ve_kup_hesapla(sayilar):
    sonuclar = [(sayi ** 2 if sayi % 2 != 0 else sayi ** 3) for sayi in sayilar]
    return sonuclar

# Örnek kullanım
sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(kare_ve_kup_hesapla(sayilar))

