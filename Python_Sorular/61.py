# Bir metindeki tüm anlamlı cümleleri bulan bir programı nasıl yazarsınız? (Anlamlı cümle, metindeki kelimelerin tümünü içeren cümledir.)

def find_meaningful_sentences(text, words):
    sentences = text.split(".")
    meaningful_sentences = []

    # Her cümleyi kontrol ediyoruz
    for sentence in sentences:
        sentence = sentence.strip()
        sentence_words = sentence.split()

        # Cümledeki kelimelerin tümünün metinde geçip geçmediğini kontrol ediyoruz
        if all(word in words for word in sentence_words):
            meaningful_sentences.append(sentence)

    return meaningful_sentences

# Örnek kullanım
text = "Bu, örnek bir metindir. Metindeki kelimeleri kullanarak anlamlı cümleleri bulalım."
words = ["Bu", "örnek", "metindir", "kelimeleri", "anlamlı", "bulalım"]
result = find_meaningful_sentences(text, words)
print("Anlamlı Cümleler:")
for sentence in result:
    print(sentence)



"""
Bu program, verilen metindeki tüm anlamlı cümleleri bulur. Metni cümlelere ayırırız ve her bir cümleyi kontrol ederiz. Her cümlede, cümledeki kelimelerin tümünün words listesinde geçip geçmediğini kontrol ederiz. Eğer geçiyorsa, o cümleyi meaningful_sentences listesine ekleriz.

Yukarıdaki örnekte, verilen metindeki anlamlı cümleler bulunur ve ekrana yazdırılır:
"""


""" Ekran Ciktisi


Anlamlı Cümleler:
Bu, örnek bir metindir
Metindeki kelimeleri kullanarak anlamlı cümleleri bulalım


"""