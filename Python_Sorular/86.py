#  Bir metindeki tüm tarihleri bulan bir programı nasıl yazarsınız?


import re

def find_dates(text):
    pattern = r'\b\d{1,2}[/.-]\d{1,2}[/.-]\d{2,4}\b'
    dates = re.findall(pattern, text)
    return dates

# Örnek kullanım
text = "Bu bir örnek metin. 02/25/2023 ve 10-15-2022 tarihlerini içeriyor."
dates = find_dates(text)
for date in dates:
    print(date)



"""
Bu programda, find_dates adında bir fonksiyon tanımlanır. Bu fonksiyon, verilen metindeki tarihleri bulmak için Regular Expression kullanır. Düzenli ifade deseni r'\b\d{1,2}[/.-]\d{1,2}[/.-]\d{2,4}\b' olarak belirlenmiştir.

Desen açıklaması:

\b : Kelime sınırlayıcısı
\d{1,2} : 1 veya 2 basamaklı rakamlar (gün ve ay)
[/.-] : Tarih elemanlarını ayıran karakterler (/, . veya -)
\d{2,4} : 2 veya 4 basamaklı rakamlar (yıl)
\b : Kelime sınırlayıcısı
re.findall fonksiyonu, metindeki tüm eşleşen ifadeleri bir liste olarak döndürür. Bu liste, for döngüsü kullanılarak yazdırılır.

Örneğin, yukarıdaki kod çalıştırıldığında, "02/25/2023" ve "10-15-2022" tarihleri metinden bulunur ve yazdırılır.
"""