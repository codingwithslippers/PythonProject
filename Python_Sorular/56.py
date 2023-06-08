# Bir listenin tüm permütasyonlarını bulan bir programı nasıl yazarsınız?

from itertools import permutations

def find_permutations(lst):
    perm_list = list(permutations(lst))
    return perm_list

# Örnek kullanım
my_list = [1, 2, 3]
permutations_list = find_permutations(my_list)

for perm in permutations_list:
    print(perm)


"""
Bu program, itertools modülündeki permutations fonksiyonunu kullanarak bir listenin tüm permütasyonlarını bulur. permutations fonksiyonu bir liste alır ve o listenin tüm permütasyonlarını üreten bir nesne döndürür. Bu nesneyi list fonksiyonuyla bir listeye dönüştürdükten sonra, elde ettiğimiz permütasyonları yazdırmak için bir döngü kullanabiliriz.

Yukarıdaki örnekte, [1, 2, 3] listesinin tüm permütasyonları elde edilir ve her bir permütasyon ekrana yazdırılır. Çıktı aşağıdaki gibi olacaktır:
"""


""" EKRAN CIKTISI

(1, 2, 3)
(1, 3, 2)
(2, 1, 3)
(2, 3, 1)
(3, 1, 2)
(3, 2, 1)


"""