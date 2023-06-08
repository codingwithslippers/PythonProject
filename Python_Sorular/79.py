# Bir sayı listesindeki tek sayıları içeren bir iterable nesne oluşturun ve bu nesneyi for döngüsü kullanarak yazdırın.

class OddNumbersIterable:
    def __init__(self, numbers):
        self.numbers = numbers
    
    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        while self.index < len(self.numbers):
            if self.numbers[self.index] % 2 != 0:
                result = self.numbers[self.index]
                self.index += 1
                return result
            self.index += 1
        raise StopIteration

# Örnek kullanım
my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_iterable = OddNumbersIterable(my_numbers)

for number in odd_iterable:
    print(number)



"""
Bu programda, OddNumbersIterable adında bir iterable sınıfı tanımlanır. Sınıfın __init__ metodunda, işlem yapılacak olan sayı listesi alınır. __iter__ metodu ise iterable olmasını sağlamak için sınıfın kendisini döndürür.

__next__ metodu ise her çağrıldığında bir sonraki tek sayıyı döndürür. Bunun için self.index değişkeni kullanılarak liste üzerinde gezinilir. Her adımda bir sonraki eleman kontrol edilir ve tek sayı ise döndürülür. Eğer döngü sona ermişse, StopIteration hatası fırlatılarak döngünün sona ermesi sağlanır.

Yukarıdaki örnekte, [1, 2, 3, 4, 5, 6, 7, 8, 9] listesindeki tek sayılar sırayla yazdırılır:
"""

"""EKRAN CIKTISI
1
3
5
7
9
"""