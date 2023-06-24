# Bir dizedeki sessiz harfleri (sesiz harfler: "aeıioöuü" dışındaki harfler) kaldıran bir Python fonksiyonu nasıl yazılır?

def sessiz_harfleri_kaldir(dize):
    sessizler = "bcçdfgğhjklmnprsştvyzxqw"
    yeni_dize = ''.join(harf for harf in dize if harf.lower() not in sessizler)
    return yeni_dize

# Örnek kullanım
dize = "Merhaba Dünya!"
print(sessiz_harfleri_kaldir(dize))
