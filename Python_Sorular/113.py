# Bir dizideki ardışık sayıların en uzun toplamını bulan bir Python fonksiyonu nasıl yazılır?

def en_uzun_ardisik_toplam(dizi):
    max_toplam = float('-inf')
    suanki_toplam = 0
    for sayi in dizi:
        suanki_toplam = max(sayi, suanki_toplam + sayi)
        max_toplam = max(max_toplam, suanki_toplam)
    return max_toplam

# Örnek kullanım
dizi = [1, -2, 3, -1, 2, -3, 4, -1]
print(en_uzun_ardisik_toplam(dizi))
