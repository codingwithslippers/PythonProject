import random

def sayisal_loto_cekilisi():
    sayilar = random.sample(range(1, 101), 6)
    print("Sayısal Loto Çekilişi Sonucu:")
    print(" ".join(map(str, sayilar)))

sayisal_loto_cekilisi()


'''

Bu programda, sayisal_loto_cekilisi() adlı bir fonksiyon tanımlanmıştır. Fonksiyon, random.sample() fonksiyonunu kullanarak 1 ile 100 arasındaki sayılardan 6 farklı sayı seçer.

Seçilen sayıları ekrana yazdırmak için print() fonksiyonunu kullanırız. Sayıları birleştirirken join() ve map() fonksiyonlarını kullanarak sayıları boşlukla ayrılmış şekilde yazdırırız.

Programı  her çalıştırmada farklı 6 sayıyı sayısal loto çekilişi sonucu olarak göreceksiniz.

'''