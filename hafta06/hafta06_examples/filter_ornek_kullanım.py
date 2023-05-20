# 5'ten büyük sayıları filtreleyen bir fonksiyon
def buyuk_5(sayi):
    return sayi > 5

# Liste üzerinde filter() fonksiyonunu kullanma
liste = [1, 8, 4, 10, 3, 6]
sonuc = filter(buyuk_5, liste)

# Sonucu liste olarak yazdırma
print(list(sonuc))  # Çıktı: [8, 10, 6]

'''
Bu örnekte, buyuk_5 adlı bir fonksiyon tanımlanmıştır. Bu fonksiyon, bir sayının 5'ten büyük olup olmadığını kontrol eder ve sonucu döndürür. filter() fonksiyonu, buyuk_5 fonksiyonunu liste üzerinde her bir öğe için uygular ve koşulu sağlayan öğeleri yeni bir filter objesi olarak döndürür. Sonucu ekrana yazdırmak için list() fonksiyonu kullanarak filter objesini bir liste haline getiririz.

Çıktı olarak [8, 10, 6] alırız, çünkü filter() fonksiyonu her bir öğeyi buyuk_5 fonksiyonuna gönderir ve sadece 5'ten büyük olanları döndürür.

filter() fonksiyonu, lambda ifadeleriyle de kullanılabilir. İşte yukarıdaki örneği lambda ifadesiyle tekrar yazarsak:

'''




