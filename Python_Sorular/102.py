# Bir dizeyi ters çeviren bir Python fonksiyonu nasıl yazılır? 

def dizeyi_ters_cevir(dize):
    ters_dize = ""
    for karakter in dize:
        ters_dize = karakter + ters_dize
    return ters_dize

# Örnek kullanım
dize = "Merhaba Dünya!"
print(dizeyi_ters_cevir(dize))
