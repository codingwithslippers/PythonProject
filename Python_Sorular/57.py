#  Bir metindeki tüm anagramları bulan bir programı nasıl yazarsınız? (Anagram:Bir kelimedeki harflerin yerleri değiştirilerek elde edilen kelime)

from collections import Counter

def find_anagrams(text):
    # Metindeki tüm kelimeleri ayırıyoruz
    words = text.split()

    # Her kelimenin karakterlerini sıralanmış bir dizeye dönüştürüyoruz
    sorted_words = [''.join(sorted(word)) for word in words]

    # Her kelimenin karakterlerinin sayısını içeren bir Counter nesnesi oluşturuyoruz
    word_counts = Counter(sorted_words)

    # Anagramları depolamak için bir sözlük kullanıyoruz
    anagram_dict = {}

    # Her kelimeyi anagramlarına göre sınıflandırıyoruz
    for word, count in word_counts.items():
        if count > 1:
            if count not in anagram_dict:
                anagram_dict[count] = [word]
            else:
                anagram_dict[count].append(word)

    # Anagramları ekrana yazdırıyoruz
    for count, anagrams in anagram_dict.items():
        print(f"Anagramlar ({count} karakter):")
        for anagram in anagrams:
            print(anagram)
        print()

# Örnek kullanım
text = "listen silent cat act tac god dog"
find_anagrams(text)

"""
Bu program, verilen metindeki tüm anagramları bulur. İlk olarak, metni kelimelere ayırırız. Ardından her bir kelimenin karakterlerini sıralanmış bir dizeye dönüştürürüz. Bu şekilde, aynı harfleri içeren kelimelerin aynı sıralanmış dizeye sahip olacağını garanti ederiz.

Daha sonra, her kelimenin sıralanmış dizelerinin sayısını saymak için Counter sınıfını kullanırız. Bu bize her bir anagram grubunun tekrar sayısını sağlar.

Son olarak, anagramları depolamak için bir sözlük kullanırız. Her bir anagram grubunu ilgili tekrar sayısına göre sınıflandırırız.

Yukarıdaki örnekte, "listen", "silent", "cat", "act", "tac", "god" ve "dog" kelimeleri birlikte çalışarak çeşitli anagram grupları oluştururlar. Program bu grupları ekrana yazdırır:
"""


""" EKRAN CIKTISI

Anagramlar (2 karakter):
tac
act

Anagramlar (3 karakter):
god
dog


"""
