# Örnek Soru 4.1: Verilen bir stringi tersten ekrana yazdıran programı yazınız.

def ters_yazdir(string):
    tersten = ""
    for harf in reversed(string):
        tersten += harf
    print(tersten)

# Örnek kullanım
metin = "Merhaba Dünya!"
ters_yazdir(metin)

