# Karesini alacak fonksiyon
def kare_al(sayi):
    return sayi ** 2

# 1'den 10'a kadar olan sayılar
sayilar = range(1, 11)

# map() fonksiyonunu kullanarak kareleri hesapla
sonuc = map(kare_al, sayilar)

# Sonucu liste olarak yazdır
print(list(sonuc))

'''
Bu programda, kare_al adlı bir fonksiyon tanımlıyoruz. Bu fonksiyon, bir sayının karesini hesaplar ve sonucu döndürür.

range(1, 11) ifadesiyle 1'den 10'a kadar olan sayıları temsil eden bir range nesnesi oluşturuyoruz.

Sonra, map() fonksiyonunu kullanarak kare_al fonksiyonunu sayilar üzerinde her bir öğe için uyguluyoruz ve sonuçları bir map nesnesi olarak alıyoruz.

Sonucu ekrana yazdırmadan önce list() fonksiyonunu kullanarak map nesnesini bir liste haline dönüştürüyoruz. Bu, map nesnesini görüntülenebilir bir liste yapar.

Programın çıktısı şu şekilde olacaktır:

[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

'''



