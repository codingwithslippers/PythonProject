# Verilen bir listenin elemanlarını küçükten büyüğe sıralayan bir Python fonksiyonu nasıl yazılır?


def sirala(liste):
    sirali_liste = sorted(liste)
    return sirali_liste

# Örnek kullanım
liste = [3, 1, 5, 2, 4]
print(sirala(liste))
