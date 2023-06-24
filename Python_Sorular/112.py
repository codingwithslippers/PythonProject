# Verilen bir listenin ardışık olmayan en büyük toplam alt dizisini bulan bir Python fonksiyonu nasıl yazılır?

def maksimum_alt_dizi(liste):
    max_toplam = float('-inf')
    suanki_toplam = 0
    for sayi in liste:
        suanki_toplam = max(sayi, suanki_toplam + sayi)
        max_toplam = max(max_toplam, suanki_toplam)
    return max_toplam

# Örnek kullanım
liste = [1, -2, 3, -1, 2, -3, 4, -1]
print(maksimum_alt_dizi(liste))
