# Verilen bir dizideki tüm öğelerin eşit olup olmadığını kontrol eden bir Python fonksiyonu nasıl yazılır?

def esit_mi(dizi):
    if len(set(dizi)) == 1:
        return True
    else:
        return False

# Örnek kullanım
dizi1 = [1, 1, 1, 1, 1]
print(esit_mi(dizi1))  # True

dizi2 = [1, 2, 3, 4, 5]
print(esit_mi(dizi2))  # False
