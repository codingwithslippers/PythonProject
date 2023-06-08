# Verilen bir metindeki tüm rakamları bulan bir programı nasıl yazarsınız?

import re

def find_digits(text):
    pattern = r'\d+'
    digits = re.findall(pattern, text)
    return digits

# Örnek kullanım
text = "Bu bir örnek metin. Metin içinde 1234 ve 5678 rakamları bulunuyor."
digits = find_digits(text)
for digit in digits:
    print(digit)

"""
Bu programda, find_digits adında bir fonksiyon tanımlanır. Bu fonksiyon, verilen metindeki tüm rakamları bulmak için Regular Expression kullanır. Düzenli ifade deseni r'\d+' olarak belirlenmiştir.

Desen açıklaması:

\d : Bir rakam karakteri eşleştirir
+ : Bir veya daha fazla rakam karakteriyle eşleştirir
re.findall fonksiyonu, metindeki tüm eşleşen ifadeleri bir liste olarak döndürür. Bu liste, for döngüsü kullanılarak yazdırılır.

Örneğin, yukarıdaki kod çalıştırıldığında, metindeki "1234" ve "5678" gibi rakamlar bulunur ve yazdırılır.




"""