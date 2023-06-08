# Verilen bir metindeki tüm e-posta adreslerini bulan bir programı nasıl yazarsınız?


import re

def find_emails(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    emails = re.findall(pattern, text)
    return emails

# Örnek kullanım
text = "Bu bir örnek metin. john@example.com ve alice@example.com adreslerini içeriyor."
emails = find_emails(text)
for email in emails:
    print(email)



"""
Bu programda, find_emails adında bir fonksiyon tanımlanır. Bu fonksiyon, verilen metindeki e-posta adreslerini bulmak için Regular Expression kullanır. Düzenli ifade deseni r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b' olarak belirlenmiştir.

Desen açıklaması:

\b : Kelime sınırlayıcısı
[A-Za-z0-9._%+-]+ : E-posta adresinin kullanıcı adı
@ : At işareti
[A-Za-z0-9.-]+ : E-posta adresinin alan adı
\. : Nokta karakteri
[A-Za-z]{2,} : E-posta adresinin üst seviye alan adı (en az 2 harf)
\b : Kelime sınırlayıcısı
re.findall fonksiyonu, metindeki tüm eşleşen ifadeleri bir liste olarak döndürür. Bu liste, for döngüsü kullanılarak yazdırılır.

Örneğin, yukarıdaki kod çalıştırıldığında, "john@example.com" ve "alice@example.com" e-posta adresleri metinden bulunur ve yazdırılır.
"""