# Bir dizideki tek sayıların karesini alan ve bunları yeni bir diziye atan bir Python fonksiyonu nasıl yazılır?

def tek_sayilarin_kareleri(dizi):
    kareler = [sayi ** 2 for sayi in dizi if sayi % 2 != 0]
    return kareler

# Örnek kullanım
dizi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(tek_sayilarin_kareleri(dizi))
