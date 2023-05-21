#Örnek Soru 6.1 ROT13 Türkçe Şifrelemesi Sorusu: Klavyeden girilen her bir karakteri ( sayı içermeyecek şekilde ) alfabede kendisinden sonra gelen 13.karakter ile değiştiren ( gerektiğinde ‘Z’ den ‘A’ ya atlayacak şekilde ) basit bir şifreleme programı yazınız.
def rot13():
    alfabe_buyuk = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
    alfabe_kucuk = "abcçdefgğhıijklmnoöprsştuüvyz"
    donus_buyuk = alfabe_buyuk[13:] + alfabe_buyuk[:13]
    donus_kucuk = alfabe_kucuk[13:] + alfabe_kucuk[:13]
    cevirme_buyuk = str.maketrans(alfabe_buyuk, donus_buyuk)
    cevirme_kucuk = str.maketrans(alfabe_kucuk, donus_kucuk)
    
    def rotKar(c):
        if c in alfabe_buyuk:
            return donus_buyuk[alfabe_buyuk.index(c)]
        elif c in alfabe_kucuk:
            return donus_kucuk[alfabe_kucuk.index(c)]
        else:
            return c
    
    return rotKar

s = input("Metni Giriniz: ")
sifreli_metin = ""
rot = rot13()
for karakter in s:
    sifreli_metin += rot(karakter)
print("Şifreli Metin:", sifreli_metin)

# Ekran Çıktısı
# Metni Giriniz: Çiğdem
# Şifreli Metin: Nusoöz


