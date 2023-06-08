# Verilen bir metindeki tüm özel karakterleri (noktalama işaretleri, boşluklar, vb.) kaldıran bir programı nasıl yazarsınız?


def remove_special_characters(text):
    special_characters = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    cleaned_text = ""

    for char in text:
        if char not in special_characters:
            cleaned_text += char

    return cleaned_text

# Örnek kullanım
text = "Merhaba, nasılsınız?"
cleaned_text = remove_special_characters(text)
print("Özel karakterler kaldırılmış metin:", cleaned_text)


"""
Bu program, verilen metindeki tüm özel karakterleri kaldırır. Programda, for döngüsü kullanarak metindeki her bir karakteri kontrol ederiz. Eğer karakter özel bir karakter değilse (char not in special_characters), o karakteri temizlenmiş metne ekleriz.

Yukarıdaki örnekte, verilen metindeki özel karakterler kaldırılarak temizlenmiş metin elde edilir ve ekrana yazdırılır:
"""

"""EKRAN CIKTISI
Özel karakterler kaldırılmış metin: Merhaba nasılsınız
"""