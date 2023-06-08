# Verilen bir metindeki tüm şifreleri bulan bir programı nasıl yazarsınız? (Belirli şifre formatına uyanları bulma)

import re

def find_passwords(text):
    pattern = r'\b(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=])\w{8,}\b'
    passwords = re.findall(pattern, text)
    return passwords

# Örnek kullanım
text = "Bu bir örnek metin. GüçlüŞifre123 ve @kompleksparola denemeleri içeriyor."
passwords = find_passwords(text)
for password in passwords:
    print(password)


"""Bu programda, find_passwords adında bir fonksiyon tanımlanır. Bu fonksiyon, verilen metindeki belirli bir şifre formatına uyan şifreleri bulmak için Regular Expression kullanır. Düzenli ifade deseni r'\b(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=])\w{8,}\b' olarak belirlenmiştir.

Desen açıklaması:

\b : Kelime sınırlayıcısı
(?=.*[A-Z]) : En az bir büyük harf içeren
(?=.*[a-z]) : En az bir küçük harf içeren
(?=.*\d) : En az bir rakam içeren
(?=.*[@#$%^&+=]) : En az bir özel karakter içeren (@, #, $, %, ^, &, + veya =)
\w{8,} : En az 8 karakter uzunluğunda olan
\b : Kelime sınırlayıcısı
re.findall fonksiyonu, metindeki tüm eşleşen ifadeleri bir liste olarak döndürür. Bu liste, for döngüsü kullanılarak yazdırılır.

Örneğin, yukarıdaki kod çalıştırıldığında, "GüçlüŞifre123" ve "@kompleksparola" gibi belirli bir şifre formatına uyan şifreler metinden bulunur ve yazdırılır. Şifre formatını ihtiyaçlarınıza göre ayarlayarak düzenli ifade desenini güncellemeniz gerekebilir."""