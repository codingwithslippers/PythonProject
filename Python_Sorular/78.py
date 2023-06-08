# İki listeyi birleştiren bir iterator sınıfı yazın. İterator, her iki listenin elemanlarını sırayla dönmelidir.

class MergeListsIterator:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.list1) + len(self.list2):
            if self.index < len(self.list1):
                result = self.list1[self.index]
            else:
                result = self.list2[self.index - len(self.list1)]
            self.index += 1
            return result
        raise StopIteration

# Örnek kullanım
my_list1 = [1, 2, 3]
my_list2 = ['a', 'b', 'c', 'd']
merge_iterator = MergeListsIterator(my_list1, my_list2)

for item in merge_iterator:
    print(item)



"""
Bu programda, MergeListsIterator adında bir iterator sınıfı tanımlanır. Sınıfın __init__ metodunda, birleştirilecek olan iki liste alınır ve iterator için gerekli değişkenler ayarlanır. __iter__ metodunda sınıfın kendisini döndürerek iterable olmasını sağlar.

__next__ metodu ise her çağrıldığında bir sonraki elemanı döndürür. Bunun için self.index değişkeni kullanılarak her bir liste sırayla işlenir. Eğer self.index değişkeni toplam eleman sayısından küçük olduğu sürece döngü devam eder. Her adımda bir sonraki eleman döndürülür. self.index değişkeni her adımda bir arttırılır. Eğer döngü sona ermişse, StopIteration hatası fırlatılarak döngünün sona ermesi sağlanır.

Yukarıdaki örnekte, [1, 2, 3] ve ['a', 'b', 'c', 'd'] listeleri birleştirilerek elemanlar sırayla yazdırılır:
"""
"""EKRAN CIKTISI
1
2
3
a
b
c
d
"""