import random

def tek_sayilari_listele(a, b):
    if a > b:
        a, b = b, a  # a'yı küçük, b'yi büyük sayıya ayarlayalım

    print(f"s1={a}")
    print(f"s2={b}")

    tek_sayilar = []
    adet = 0

    for sayi in range(a, b+1):
        if sayi % 2 != 0:  # Tek sayıları kontrol edelim
            tek_sayilar.append(sayi)
            adet += 1

    print(" ".join(map(str, tek_sayilar)))  # Tek sayıları boşlukla ayrılmış şekilde yazdıralım
    print("Toplam tek sayı adedi:", adet)

s1 = random.randint(1, 100)
s2 = random.randint(1, 100)

tek_sayilari_listele(s1, s2)


'''
Bu programda, tek_sayilari_listele(a, b) adlı bir fonksiyon tanımlanmıştır. Fonksiyon, a ve b parametreleri arasındaki sayıları kontrol ederek tek sayıları listeleyip adedini verir.

Programın ana kısmında, s1 ve s2 değişkenleri rastgele olarak 1 ile 100 arasında seçilir. Ardından, tek_sayilari_listele() fonksiyonu bu değerleri alarak çağrılır.

Fonksiyon içinde, a ve b değerlerini ekrana yazdırırız. Daha sonra, for döngüsü ile a ve b arasındaki sayıları kontrol ederiz. Her bir sayıyı kontrol ederken, tek olup olmadığını kontrol ederiz (sayi % 2 != 0). Tek sayıları tek_sayilar listesine ekleriz ve aynı zamanda adedini tutmak için adet değişkenini artırırız.

Son olarak, tek_sayilar listesini boşlukla ayrılmış şekilde ekrana yazdırırız ve toplam tek sayı adedini gösteririz.

Programı çalıştırdığınızda, rastgele seçilen s1 ve s2 değerlerine göre aralarında bulunan tek sayıları ve adedini göreceksiniz.

'''