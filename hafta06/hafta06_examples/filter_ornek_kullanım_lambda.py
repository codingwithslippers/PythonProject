liste = [1, 8, 4, 10, 3, 6]
sonuc = filter(lambda x: x > 5, liste)
print(list(sonuc))  # Çıktı: [8, 10, 6]


'''
Bu örnekte, lambda ifadesi x parametresinin değerinin 5'ten büyük olup olmadığını kontrol eder. Bu ifade x > 5 şeklinde verilmiştir. filter() fonksiyonu, bu lambda ifadesini liste üzerindeki her bir öğe için uygular ve koşulu sağlayan öğeleri döndürür.

Yani, filter(lambda x: x > 5, liste) ifadesi liste içindeki her bir öğe için x > 5 koşulunu kontrol eder. 5'ten büyük olan öğeler bu koşulu sağlar ve sonuç olarak [8, 10, 6] gibi bir liste elde ederiz.

iterable terimi, üzerinde döngü işlemi gerçekleştirilebilen veya parçalara ayrılabilen bir veri yapısını ifade eder. Liste, demet, dize gibi veri yapıları, Python'da iterable olarak kabul edilir. filter() fonksiyonu, üzerinde işlem yapabileceğimiz bir iterable'ı alır ve her bir öğe için belirtilen koşulu uygular.

'''