import random

def obeb_hesapla(m, n):
    if m < n:
        m, n = n, m  # m'yi büyük, n'yi küçük sayıya ayarlayalım

    while n != 0:
        m, n = n, m % n

    return m

# Rastgele iki sayı seçelim
m = random.randint(1, 100)
n = random.randint(1, 100)

# Seçilen sayıları ekrana yazdıralım
print(f"m = {m}")
print(f"n = {n}")

# OBEB'i hesaplayalım
obeb = obeb_hesapla(m, n)

# Sonucu ekrana yazdıralım
print(f"OBEB(m, n) = {obeb}")

'''

Bu programda, obeb_hesapla(m, n) adlı bir fonksiyon tanımlanmıştır. Fonksiyon, verilen m ve n sayıları için OBEB hesaplar ve sonucu döndürür. Hesaplama için Euclid Algoritması kullanılır.

Programın ana kısmında, m ve n değişkenleri rastgele olarak 1 ile 100 arasında seçilir. Ardından, seçilen sayıları ekrana yazdırırız.

obeb_hesapla() fonksiyonunu m ve n değerleriyle çağırarak OBEB'i hesaplarız ve sonucu obeb değişkenine atarız.

Son olarak, hesaplanan OBEB'i ekrana yazdırırız.

Programı çalıştırdığınızda, rastgele seçilen m ve n değerlerine göre OBEB'ini göreceksiniz.

'''