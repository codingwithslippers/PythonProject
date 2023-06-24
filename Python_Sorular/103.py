# Bir dizideki en büyük iki sayıyı bulan bir Python fonksiyonu nasıl yazılır?

def en_buyuk_iki_sayi(dizi):
    en_buyuk = float('-inf')
    ikinci_en_buyuk = float('-inf')
    for sayi in dizi:
        if sayi > en_buyuk:
            ikinci_en_buyuk = en_buyuk
            en_buyuk = sayi
        elif sayi > ikinci_en_buyuk:
            ikinci_en_buyuk = sayi
    return en_buyuk, ikinci_en_buyuk

# Örnek kullanım
dizi = [1, 5, 2, 9, 3, 7]
print(en_buyuk_iki_sayi(dizi))
