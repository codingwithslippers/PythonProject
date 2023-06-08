# Bir metindeki tüm URL'leri bulan bir programı nasıl yazarsınız?

import re

def find_urls(text):
    pattern = r'\b(?:https?://|www\.)\S+\b'
    urls = re.findall(pattern, text)
    return urls

# Örnek kullanım
text = "Bu bir örnek metin. www.example.com ve https://www.google.com adreslerini içeriyor."
urls = find_urls(text)
for url in urls:
    print(url)

"""
Bu programda, find_urls adında bir fonksiyon tanımlanır. Bu fonksiyon, verilen metindeki URL'leri bulmak için Regular Expression kullanır. Düzenli ifade deseni r'\b(?:https?://|www\.)\S+\b' olarak belirlenmiştir.

Desen açıklaması:

\b : Kelime sınırlayıcısı
(?:https?://|www\.) : "http://", "https://", veya "www." ile başlayan URL'leri eşleştirir
\S+ : URL'nin geri kalanını (boşluk olmayan karakterler) eşleştirir
\b : Kelime sınırlayıcısı
re.findall fonksiyonu, metindeki tüm eşleşen ifadeleri bir liste olarak döndürür. Bu liste, for döngüsü kullanılarak yazdırılır.

Örneğin, yukarıdaki kod çalıştırıldığında, "www.example.com" ve "https://www.google.com" URL'leri metinden bulunur ve yazdırılır.
"""
