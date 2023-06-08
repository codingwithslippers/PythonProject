# Bir listedeki tüm ardışık sayıların toplamını bulan bir programı nasıl yazarsınız?


def find_sum_of_consecutive_numbers(nums):
    total_sum = 0

    for i in range(len(nums)):
        current_sum = 0
        for j in range(i, len(nums)):
            current_sum += nums[j]
            total_sum += current_sum

    return total_sum

# Örnek kullanım
my_list = [1, 2, 3, 4]
result = find_sum_of_consecutive_numbers(my_list)
print("Toplam:", result)



"""
Bu program, verilen bir listedeki tüm ardışık sayıların toplamını bulur. İç içe iki döngü kullanarak her bir ardışık sayı dizisini hesaplar ve toplamını total_sum değişkenine ekler.

İlk döngü, listenin her bir elemanını temsil eder (i). İkinci döngü ise, i'den başlayarak listenin geri kalanındaki tüm elemanları tarar (j). İç içe döngüyü kullanarak tüm ardışık sayı dizilerini buluruz.

Her bir ardışık sayı dizisi için, current_sum değişkeni kullanılarak ardışık sayıların toplamı hesaplanır. Bu toplam, total_sum değişkenine eklenir.

Yukarıdaki örnekte, [1, 2, 3, 4] listesindeki ardışık sayıların toplamı bulunur ve sonuç olarak 10 elde edilir.

Programı farklı listelerle kullanarak, herhangi bir listedeki tüm ardışık sayıların toplamını bulabilirsiniz.
"""