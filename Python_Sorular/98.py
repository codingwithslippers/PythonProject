# Verilen bir listenin medyanını bulan bir programı nasıl yazarsınız? (Medyan, listedeki elemanların ortasındaki sayıdır.)

"""
İlk olarak, listenizi sıralayın, böylece elemanlar küçükten büyüğe doğru bir sıralama alır.

Listenin uzunluğunu kontrol edin:

Eğer listenin uzunluğu tek ise, medyan doğrudan listenin ortasındaki elemandır.
Eğer listenin uzunluğu çift ise, medyan iki ortadaki elemanın aritmetik ortalamasıdır.

"""

def find_median(numbers):
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)

    if length % 2 == 1:
        # Uzunluk tek ise, medyan ortadaki elemandır
        median = sorted_numbers[length // 2]
    else:
        # Uzunluk çift ise, medyan iki ortadaki elemanın ortalamasıdır
        middle_right = length // 2
        middle_left = middle_right - 1
        median = (sorted_numbers[middle_left] + sorted_numbers[middle_right]) / 2

    return


# Örnek kullanım
numbers = [3, 1, 7, 5, 2, 6, 4]
median = find_median(numbers)
print("Medyan:", median)


"""
Bu program, verilen listenin medyanını bulmak için önce listeyi sıralar ve ardından listenin uzunluğuna bağlı olarak medyanı hesaplar. Sonuç olarak, listenin medyanını ekrana yazdırır. Yukarıdaki örnekte, verilen liste [3, 1, 7, 5, 2, 6, 4] olduğunda, program çıktı olarak "Medyan: 4" yazdıracaktır.
"""