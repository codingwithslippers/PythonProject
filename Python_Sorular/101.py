# Verilen bir listede tekrar eden sayıları bulan bir Python fonksiyonu nasıl yazılır?

def tekrar_edenleri_bul(liste):
    tekrarlar = []
    for i in range(len(liste)):
        if liste.count(liste[i]) > 1 and liste[i] not in tekrarlar:
            tekrarlar.append(liste[i])
    return tekrarlar

# Örnek kullanım
liste = [1, 2, 3, 2, 4, 3, 5, 6, 1]
print(tekrar_edenleri_bul(liste))
