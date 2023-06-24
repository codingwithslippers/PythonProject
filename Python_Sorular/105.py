# Bir dizedeki harfleri ve harflerin kaç kez tekrarlandığını hesaplayan bir Python fonksiyonu nasıl yazılır?

def harf_sayilarini_hesapla(dize):
    harf_sayilari = {}
    for harf in dize:
        if harf in harf_sayilari:
            harf_sayilari[harf] += 1
        else:
            harf_sayilari[harf] = 1
    return harf_sayilari

# Örnek kullanım
dize = "Merhaba"
print(harf_sayilarini_hesapla(dize))
