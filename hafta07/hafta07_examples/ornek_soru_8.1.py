# Örnek Soru 8.1 Polindrom Uygulama Sorusu: Girilen bir  metnin Palindrom olup olmadığını bulan programı yazınız.
def is_palindrome(text):
    # Metni temizle: Rakam, boşluk ve noktalama işaretlerini kaldır
    cleaned_text = ''.join(char.lower() for char in text if char.isalpha())
    # Temizlenmiş metni tersten al
    reversed_text = cleaned_text[::-1]
    # Temizlenmiş metin ile tersten alınmış metni karşılaştır
    if cleaned_text == reversed_text:
        return True
    else:
        return False

# Kullanıcıdan metni al
text = input("Metni Giriniz: ")
# Palindrom kontrolü yap
if is_palindrome(text):
    print("Girilen metin palindromiktir.")
else:
    print("Girilen metin palindromik değildir.")

# Ekran Çıktısı
# Metni Giriniz: anna
# Girilen metin palindromiktir.

# Ekran Çıktısı
# Metni Giriniz: adanada
# Girilen metin palindromiktir.


