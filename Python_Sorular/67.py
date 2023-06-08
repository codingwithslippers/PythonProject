# Verilen bir listedeki en büyük sayının konumunu (indeksini) bulan bir programı nasıl yazarsınız?

def find_max_index(numbers):
    max_number = float("-inf")
    max_index = -1

    for i in range(len(numbers)):
        if numbers[i] > max_number:
            max_number = numbers[i]
            max_index = i

    return max_index

# Örnek kullanım
numbers = [10, 5, 25, 8, 15]
max_index = find_max_index(numbers)
print("En büyük sayının konumu (indeksi):", max_index)


"""
Bu program, verilen listedeki en büyük sayının konumunu (indeksini) bulur. Programda, for döngüsü kullanarak listenin her bir elemanını kontrol ederiz. Eğer eleman, mevcut en büyük sayıdan daha büyükse, en büyük sayıyı ve indeksi güncelleriz.

Yukarıdaki örnekte, verilen listedeki en büyük sayının konumu (indeksi) bulunur ve ekrana yazdırılır:
"""

"""EKRAN CIKTISI
En büyük sayının konumu (indeksi): 2
"""