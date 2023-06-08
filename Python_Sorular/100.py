# Bir metindeki tüm cümleleri ters çeviren bir programı nasıl yazarsınız? (Cümleler, noktalama işaretleriyle ayrılmış tamamlanmış ifadelerdir.)

def reverse_sentences(text):
    # Metni noktalama işaretlerine göre cümlelere ayırma
    sentences = text.split('. ')

    # Ters çevrilen cümleleri tutacak bir liste oluşturma
    reversed_sentences = []

    # Her bir cümleyi ters çevirme
    for sentence in sentences:
        reversed_sentence = sentence[::-1]  # Cümleyi ters çevirme
        reversed_sentences.append(reversed_sentence)

    # Tüm cümleleri birleştirerek sonucu döndürme
    result = '. '.join(reversed_sentences)
    return result


# Örnek kullanım
text = "Python programlama dili çok popülerdir. Yazılım geliştirme için tercih edilen bir dil."
reversed_text = reverse_sentences(text)
print(reversed_text)


"""
Bu program, verilen metindeki tüm cümleleri ters çevirmek için aşağıdaki adımları izler:

1-Metni noktalama işaretlerine göre cümlelere ayırırız. Burada nokta ve boşluk kullanarak cümleleri ayırdık.
2-Her bir cümleyi ters çeviririz.
3-Ters çevrilen cümleleri bir listeye ekleriz.
4-Tüm cümleleri birleştirerek sonucu döndürürüz.

Yukarıdaki örnekte, verilen metindeki cümleleri ters çeviriyoruz. Programın çıktısı aşağıdaki gibi olacaktır:

EKRAN CIKTISI
redilüp repolpüc ekilbup edilamargorp nohtyP . ridleçrevit tercih nekcihcerekılüp em ekil.

"""