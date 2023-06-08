# Verilen bir metindeki tüm kelimelerin frekansını hesaplayan bir programı nasıl yazarsınız?

def calculate_word_frequency(text):
    word_frequency = {}

    # Metni kelimelere ayırıyoruz
    words = text.split()

    # Her kelimenin frekansını hesaplıyoruz
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    return word_frequency

# Örnek kullanım
text = "Bu bir örnek metindir. Metni kullanarak frekansları hesaplayalım."
frequency = calculate_word_frequency(text)

# Frekansları ekrana yazdırma
for word, count in frequency.items():
    print(f"{word}: {count}")


"""
Bu program, verilen metindeki tüm kelimelerin frekansını hesaplar. Metni kelimelere ayırırız ve her kelimeyi kontrol ederek frekansını hesaplarız. Her kelimeyi bir sözlükte (word_frequency) anahtar olarak kullanırız ve frekansı değer olarak saklarız. Eğer kelime zaten sözlükte bulunuyorsa, frekansını bir artırırız. Eğer kelime sözlükte yoksa, frekansını 1 olarak başlatırız.

Yukarıdaki örnekte, verilen metindeki kelimelerin frekansı hesaplanır ve ekrana yazdırılır:
"""

"""EKRAN CIKTISI

Bu: 1
bir: 1
örnek: 1
metindir.: 1
Metni: 1
kullanarak: 1
frekansları: 1
hesaplayalım.: 1

"""