# Bir liste içindeki tekrar eden elemanları bulmak için Python'da bir algoritma nasıl tasarlanır? (Zaman ve bellek karmaşıklığı optimize edilmelidir)


# Set kullanarak tekrar eden elemanları bulmak:
def tekrar_edenler(liste):
    tekrar_edenler = set()
    onceki_elemanlar = set()

    for eleman in liste:
        if eleman in onceki_elemanlar:
            tekrar_edenler.add(eleman)
        else:
            onceki_elemanlar.add(eleman)

    return list(tekrar_edenler)



# Dictionary kullanarak tekrar eden elemanları bulmak:

def tekrar_edenler(liste):
    tekrar_edenler = []
    elemanlar_sayisi = {}

    for eleman in liste:
        if eleman in elemanlar_sayisi:
            elemanlar_sayisi[eleman] += 1
        else:
            elemanlar_sayisi[eleman] = 1

    for eleman, sayi in elemanlar_sayisi.items():
        if sayi > 1:
            tekrar_edenler.append(eleman)

    return tekrar_edenler
