# Bir dizede geçen anagram kelimeleri bulan bir Python fonksiyonu nasıl yazılır?

from collections import defaultdict

def anagram_kelimeleri_bul(dize):
    kelimeler = dize.split()
    anagramlar = defaultdict(list)
    for kelime in kelimeler:
        sırali_kelime = ''.join(sorted(kelime))
        anagramlar[sırali_kelime].append(kelime)
    return [grup for grup in anagramlar.values() if len(grup) > 1]

# Örnek kullanım
dize = "elma kedi mela kedisi ekmek lima kase ekmeği kale"
print(anagram_kelimeleri_bul(dize))
