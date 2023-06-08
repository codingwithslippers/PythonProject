# Verilen bir listedeki çift sayıları içeren bir iterable nesne oluşturun.

class EvenNumbersIterable:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.index < len(self.numbers):
            number = self.numbers[self.index]
            self.index += 1
            if number % 2 == 0:
                return number
        raise StopIteration

# Örnek kullanım
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = EvenNumbersIterable(numbers)

for number in even_numbers:
    print(number)


"""

Bu programda, EvenNumbersIterable adında bir iterable sınıf tanımlanır. Sınıfın __init__ metodunda, verilen listedeki çift sayıları içeren bir iterable nesne oluşturmak için gerekli hazırlıklar yapılır. __iter__ metodunda sınıfın kendisini döndürerek iterable olmasını sağlar.

__next__ metodu ise her çağrıldığında bir sonraki çift sayıyı döndürür. Bunun için while döngüsü kullanılır ve listenin sonuna gelene kadar her eleman kontrol edilir. Eğer eleman çiftse, o eleman döndürülür. Eğer listenin sonuna gelinmişse, StopIteration hatası fırlatılarak döngünün sona ermesi sağlanır.

Yukarıdaki örnekte, verilen liste [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] olduğunda, sadece çift sayılar olan [2, 4, 6, 8, 10] çıktısı alınır.

Bu şekilde, verilen bir listedeki çift sayıları içeren bir iterable nesne oluşturmuş oluruz.

"""