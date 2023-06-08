# Verilen bir metindeki tüm telefon numaralarını bulan bir programı nasıl yazarsınız?


import re

def find_phone_numbers(text):
    pattern = r'\b\d{3}-\d{3}-\d{4}\b'
    phone_numbers = re.findall(pattern, text)
    return phone_numbers

# Örnek kullanım
text = "Bu bir örnek metin. Telefon numaraları arasında 123-456-7890 ve 555-1234 bulunuyor."
phone_numbers = find_phone_numbers(text)
for number in phone_numbers:
    print(number)


"""Bu programda, find_phone_numbers adında bir fonksiyon tanımlanır. Bu fonksiyon, verilen metindeki belirli bir telefon numarası formatına uyan telefon numaralarını bulmak için Regular Expression kullanır. Düzenli ifade deseni r'\b\d{3}-\d{3}-\d{4}\b' olarak belirlenmiştir.

Desen açıklaması:

\b : Kelime sınırlayıcısı
\d{3} : Üç rakam karakteri eşleştirir
- : Tire karakteri eşleştirir
\d{3} : Üç rakam karakteri eşleştirir
- : Tire karakteri eşleştirir
\d{4} : Dört rakam karakteri eşleştirir
\b : Kelime sınırlayıcısı
re.findall fonksiyonu, metindeki tüm eşleşen ifadeleri bir liste olarak döndürür. Bu liste, for döngüsü kullanılarak yazdırılır.

Örneğin, yukarıdaki kod çalıştırıldığında, metindeki "123-456-7890" ve "555-1234" gibi telefon numaraları bulunur ve yazdırılır. Telefon numarası formatını ihtiyaçlarınıza göre ayarlayarak düzenli ifade desenini güncellemeniz gerekebilir.
"""