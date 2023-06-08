# Bir metindeki en sık kullanılan kelimeleri ve sayılarını bulan bir Python programı nasıl yazılır? (Dikkat: Kelime sıklığı, büyük veri kümelerinde verimli bir şekilde hesaplanmalıdır)

from collections import Counter
import re

def en_sik_kelimeler(metin, n=5):
    # Metindeki kelimeleri ayırma
    kelimeler = re.findall(r'\w+', metin.lower())
    
    # Kelime sıklıklarını hesaplama
    kelime_siklikleri = Counter(kelimeler)
    
    # En sık kullanılan kelimeleri ve sayılarını almak
    en_sik_kelimeler = kelime_siklikleri.most_common(n)
    
    return en_sik_kelimeler

# Örnek kullanım
metin = "Bir metindeki kelimelerin sıklığını bulmak için Python programı yazıyoruz. Yazılımda kelime sayma işlemleri için Counter sınıfını kullanıyoruz."
en_sikler = en_sik_kelimeler(metin)

print("En sık kullanılan kelimeler:")
for kelime, sayi in en_sikler:
    print(kelime, "-", sayi)
