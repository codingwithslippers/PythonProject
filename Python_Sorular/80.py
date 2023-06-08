# Verilen bir sözlükteki tüm anahtarları içeren bir iterable nesne oluşturun ve bu nesneyi for döngüsü kullanarak yazdırın.

class KeysIterable:
    def __init__(self, dictionary):
        self.dictionary = dictionary
    
    def __iter__(self):
        self.keys = list(self.dictionary.keys())
        self.index = 0
        return self
    
    def __next__(self):
        if self.index < len(self.keys):
            result = self.keys[self.index]
            self.index += 1
            return result
        raise StopIteration

# Örnek kullanım
my_dict = {"a": 1, "b": 2, "c": 3}
keys_iterable = KeysIterable(my_dict)

for key in keys_iterable:
    print(key)



"""
Bu programda, KeysIterable adında bir iterable sınıfı tanımlanır. Sınıfın __init__ metodunda, işlem yapılacak olan sözlük alınır. __iter__ metodu ise iterable olmasını sağlamak için anahtarları liste halinde alır ve self.keys değişkenine atar. Ardından, self.index değişkeni sıfırlanarak döngüye başlanır.

__next__ metodu ise her çağrıldığında bir sonraki anahtarı döndürür. Bunun için self.index değişkeni kullanılarak anahtarlar üzerinde gezinilir. Her adımda bir sonraki anahtar döndürülür. Eğer döngü sona ermişse, StopIteration hatası fırlatılarak döngünün sona ermesi sağlanır.

Yukarıdaki örnekte, {"a": 1, "b": 2, "c": 3} sözlüğündeki anahtarlar sırayla yazdırılır:"""

"""EKRAN CIKTISI
a
b
c
"""