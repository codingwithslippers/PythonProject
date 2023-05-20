import random

sayilar = random.sample(range(7, 78), 7)

for sayi in sayilar:
    print(sayi)



'''

Bu programda, random modülünü kullanarak rastgele sayılar üretiyoruz. random.sample(range(7, 78), 7) ifadesi, 7 ile 77 arasındaki (77 dahil) tamsayılar arasından 7 adet rastgele sayı seçer.

Sonra, for döngüsüyle her bir sayıyı sayilar listesinden alarak ekrana yazdırıyoruz.

Programı çalıştırdığınızda, 7 ile 77 arasında rastgele seçilen 7 adet tamsayıyı ekranda göreceksiniz.

'''