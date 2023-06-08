#  Bir dizeyi ters çeviren ve her karakterini tek tek veren bir iterator sınıfı yazın. Bir dizeyi ters çeviren ve her karakterini tek tek veren bir iterator sınıfı yazın.

class ReverseStringIterator:
    def __init__(self, string):
        self.string = string
        self.index = len(string)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index > 0:
            self.index -= 1
            return self.string[self.index]
        raise StopIteration

# Örnek kullanım
my_string = "Hello, World!"
reverse_iterator = ReverseStringIterator(my_string)

for char in reverse_iterator:
    print(char)


"""
Bu programda, ReverseStringIterator adında bir iterator sınıfı tanımlanır. Sınıfın __init__ metodunda, ters çevrilecek olan dize alınır ve iterator için gerekli değişkenler ayarlanır. __iter__ metodunda sınıfın kendisini döndürerek iterable olmasını sağlar.

__next__ metodu ise her çağrıldığında bir sonraki karakteri döndürür. Bunun için self.index değişkeni kullanılarak dizenin sonundan başlayarak her bir karakter sırayla döndürülür. self.index değişkeni her adımda bir azaltılır. Eğer self.index sıfırdan büyük olduğu sürece döngü devam eder. Eğer döngü sona ermişse, StopIteration hatası fırlatılarak döngünün sona ermesi sağlanır.


"""

# Yukarıdaki örnekte, "Hello, World!" dizesi ters çevrilerek her karakter ayrı ayrı yazdırılır:

"""EKRAN CIKTISI
!
d
l
r
o
W
,
o
l
l
e
H
"""