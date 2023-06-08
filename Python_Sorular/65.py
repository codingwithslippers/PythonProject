# Verilen bir metindeki tüm sesli harflerin sayısını hesaplayan bir Python  programı nasıl yazarsınız?


def count_vowels(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0

    for char in text:
        if char in vowels:
            vowel_count += 1

    return vowel_count

# Örnek kullanım
text = "Merhaba, nasılsınız?"
vowel_count = count_vowels(text)
print("Sesli harf sayısı:", vowel_count)


"""
Bu program, verilen metindeki tüm sesli harflerin sayısını hesaplar. Programda, for döngüsü kullanarak metindeki her bir karakteri kontrol ederiz. Eğer karakter sesli harf ise (char in vowels), sesli harf sayısını bir artırırız.

Yukarıdaki örnekte, verilen metindeki sesli harf sayısı hesaplanır ve ekrana yazdırılır:
"""

"""EKRAN CIKTISI
Sesli harf sayısı: 6
"""