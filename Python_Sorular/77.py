# Bir listenin tüm elemanlarının karesini alan bir map iterator sınıfı yazın.

class SquareMapIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.iterable):
            result = self.iterable[self.index] ** 2
            self.index += 1
            return result
        raise StopIteration

# Örnek kullanım
my_list = [1, 2, 3, 4, 5]
square_iterator = SquareMapIterator(my_list)

for num in square_iterator:
    print(num)



"""
Bu programda, SquareMapIterator adında bir iterator sınıfı tanımlanır. Sınıfın __init__ metodunda, işlem yapılacak olan iterable alınır ve iterator için gerekli değişkenler ayarlanır. __iter__ metodunda sınıfın kendisini döndürerek iterable olmasını sağlar.

__next__ metodu ise her çağrıldığında bir sonraki elemanın karesini döndürür. Bunun için self.iterable üzerindeki elemanlar tek tek işlenir. Eğer self.index değişkeni listenin boyutundan küçük olduğu sürece döngü devam eder. Her adımda bir sonraki elemanın karesi hesaplanır ve döndürülür. self.index değişkeni her adımda bir arttırılır. Eğer döngü sona ermişse, StopIteration hatası fırlatılarak döngünün sona ermesi sağlanır.

Yukarıdaki örnekte, [1, 2, 3, 4, 5] listesinin elemanlarının kareleri sırasıyla hesaplanarak yazdırılır:
"""

"""EKRAN CIKTISI
1
4
9
16
25
"""