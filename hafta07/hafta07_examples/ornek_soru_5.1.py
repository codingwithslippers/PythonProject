# Örnek Soru 5.1 Cümledeki Kelime ve Harf Sayısını Öğrenme Sorusu:  Girilen bir cümledeki harflerin ve kelimelerin sayısını veren programı yazınız. 

def harf_ve_kelime_sayisi(cumle):
    harf_sayisi = len(cumle.replace(" ", ""))
    kelime_sayisi = len(cumle.split())
    
    print("Harf sayısı:", harf_sayisi)
    print("Kelime sayısı:", kelime_sayisi)

# Örnek kullanım
cumle = input("Bir cümle girin: ")
harf_ve_kelime_sayisi(cumle)


