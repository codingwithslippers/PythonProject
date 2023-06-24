# Bir dizedeki harfleri alfabedeki bir sonraki harfle değiştiren bir Python fonksiyonu nasıl yazılır?

def harfleri_degistir(dize):
    yeni_dize = ""
    for harf in dize:
        if harf.isalpha():
            yeni_harf = chr((ord(harf) - 97 + 1) % 26 + 97)
            yeni_dize += yeni_harf
        else:
            yeni_dize += harf
    return yeni_dize

# Örnek kullanım
dize = "abcxyz"
print(harfleri_degistir(dize))
