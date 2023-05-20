import random

def sayi_tahmin_oyunu():
    dogru_sayi = random.randint(0, 100)
    tahminler = []
    puan = 100

    while True:
        tahmin = int(input("İlk tahmininiz: "))
        tahminler.append(tahmin)

        if tahmin < dogru_sayi:
            print("Daha büyük bir sayı giriniz!")
        elif tahmin > dogru_sayi:
            print("Daha küçük bir sayı giriniz!")
        else:
            print(f"Bravo! {len(tahminler)}.de {dogru_sayi} i bildiniz")
            break

        puan -= 10

    print("Puanınız:", puan)

sayi_tahmin_oyunu()


'''

Bu programda, sayi_tahmin_oyunu() adlı bir fonksiyon tanımlanmıştır. Fonksiyon, rastgele bir sayı seçer ve kullanıcının tahminlerini kontrol ederek doğru sayıyı bulmasını sağlar.

Oyun, bir while döngüsü içinde çalışır ve kullanıcı doğru sayıyı bulana kadar devam eder. Her tahmin sonrasında, tahminin doğruluğuna göre bir geri bildirim verilir (daha büyük veya daha küçük sayı giriniz). Tahminler ve puan takip edilir.

Doğru sayıyı bulduğunda, doğru sayıyı ve kaçıncı tahminde bulduğunu gösteren bir tebrik mesajı verilir. Ardından, puan ekrana yazdırılır.

Programı çalıştırdığınızda, kullanıcıdan tahminler alacak ve istenilen geri bildirimi verecektir. Doğru sayıyı bulduğunda, kaçıncı tahminde bulunduğunu ve puanınızı göreceksiniz.

'''