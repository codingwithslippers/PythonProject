# Verilen bir sayının asal olup olmadığını kontrol eden bir Python fonksiyonu nasıl yazılır?

def asal_mi(sayi):
    if sayi < 2:
        return False
    for i in range(2, int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            return False
    return True

# Örnek kullanım
sayi = 17
print(asal_mi(sayi))
