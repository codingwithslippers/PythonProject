# Bir listedeki en büyük ikinci sayıyı bulan bir programı nasıl yazarsınız?

# Yaklaşım: Listeyi sıralamak


def find_second_largest(nums):
    nums.sort(reverse=True)
    return nums[1] if len(nums) > 1 else None

# Örnek kullanım
my_list = [5, 3, 9, 1, 7]
result = find_second_largest(my_list)
print("En büyük ikinci sayı:", result)

"""
Bu program, verilen listedeki en büyük ikinci sayıyı bulmak için listeyi sıralar ve ardından ikinci elemanı döndürür. Önceki yaklaşım, listenin orijinal sırasını değiştirir.
"""


# Yaklaşım: Döngü kullanmak

def find_second_largest(nums):
    max_num = float('-inf')
    second_max = float('-inf')

    for num in nums:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif num > second_max and num < max_num:
            second_max = num

    return second_max if second_max != float('-inf') else None

# Örnek kullanım
my_list = [5, 3, 9, 1, 7]
result = find_second_largest(my_list)
print("En büyük ikinci sayı:", result)


"""
Bu program, verilen listedeki en büyük ikinci sayıyı bulmak için bir döngü kullanır. İki değişken (max_num ve second_max) kullanarak en büyük ve ikinci en büyük sayıları günceller. Döngü boyunca, her elemanı kontrol eder ve uygun durumlarda değişkenleri günceller.

Her iki yaklaşım da listenin tüm elemanlarını kontrol eder ve en büyük ikinci sayıyı bulur. İkinci yaklaşım, orijinal listenin sırasını değiştirmese de, her elemanı kontrol etmek için bir döngü kullanır.

Her iki örnekte de, [5, 3, 9, 1, 7] listesindeki en büyük ikinci sayı bulunur ve sonuç olarak 7 elde edilir.

Programı farklı listelerle kullanarak, herhangi bir listedeki en büyük ikinci sayıyı bulabilirsiniz.
"""