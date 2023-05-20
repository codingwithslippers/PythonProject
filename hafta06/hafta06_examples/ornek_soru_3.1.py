def harf_sayisi(metin):
    harf_sozluk = {}
    for harf in metin:
        if harf.isalpha():
            if harf in harf_sozluk:
                harf_sozluk[harf] += 1
            else:
                harf_sozluk[harf] = 1
    return harf_sozluk

# Kullanıcıdan metin dizisini alın
metin = input("Metin dizisini girin: ")

# Harf sayısını hesaplayın
sonuc = harf_sayisi(metin)

# Sonucu ekrana yazdırın
for harf, sayi in sonuc.items():
    print(harf, ":", sayi)

"""
harf_sayisi adlı bir fonksiyon tanımlanır. Bu fonksiyon, metin dizisini parametre olarak alır. Bir boş sözlük (harf_sozluk) oluşturulur.

Metin dizisini döngüye alırken her karakter için şu işlemler yapılır:

isalpha() fonksiyonunu kullanarak karakterin bir harf olup olmadığını kontrol eder.
Eğer karakter bir harfse, sözlükte bu harf var mı diye kontrol eder:
Eğer harf zaten sözlükte varsa, sayısını bir artırır.
Eğer harf sözlükte yoksa, sözlüğe yeni bir giriş yapar ve sayısını 1 olarak ayarlar.
Döngü tamamlandıktan sonra, harf_sozluk sözlüğünü döndürür.

Ana programda kullanıcıdan metin dizisini alır.

harf_sayisi fonksiyonunu çağırarak metindeki harf sayılarını hesaplar ve sonucu sonuc değişkenine atar.

Sonucu ekrana yazdırmak için bir döngü kullanılır. Her harf ve sayısı items() fonksiyonuyla alınır ve print() fonksiyonuyla ekrana yazdırılır.

Örneğin, kullanıcı tarafından girilen metin "Merhaba Dünya!" ise, program şu çıktıyı üretecektir.
"""