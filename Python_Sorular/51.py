# Bir listedeki en uzun ardışık artan alt diziyi bulan bir Python programı nasıl yazılır?


def en_uzun_artan_alt_dizi(liste):
    n = len(liste)
    lengths = [1] * n
    indexes = [-1] * n
    max_length = 1
    max_index = 0

    for i in range(1, n):
        for j in range(i):
            if liste[i] > liste[j] and lengths[i] < lengths[j] + 1:
                lengths[i] = lengths[j] + 1
                indexes[i] = j

        if lengths[i] > max_length:
            max_length = lengths[i]
            max_index = i

    alt_dizi = []
    while max_index != -1:
        alt_dizi.append(liste[max_index])
        max_index = indexes[max_index]

    alt_dizi.reverse()
    return alt_dizi

# Örnek kullanım
liste = [1, 3, 2, 5, 8, 7, 9, 10, 12]
uzun_alt_dizi = en_uzun_artan_alt_dizi(liste)
print("En uzun ardışık artan alt dizi:", uzun_alt_dizi)
