# try-except bloklarının yapısı nasıldır ve nasıl kullanılır? Ornek kod bloklari vererek aciklayiniz?

"""

try-except blokları, bir programın belirli bir kod bloğunda hata oluşma potansiyeli olan bölümleri tanımlamak ve bu hataları ele almak için kullanılır. try bloğunda potansiyel bir hata oluşabilecek kodlar yer alırken, except bloğu hata oluştuğunda çalışacak olan kodları içerir. 

"""

# Örnek 1: Sadece bir hata türünü ele almak için try-except kullanımı
try:
    # Potansiyel hata oluşabilecek kodlar
    x = int(input("Bir sayı girin: "))
    result = 10 / x
    print("Sonuç:", result)
except ZeroDivisionError:
    # Hata durumunda çalışacak kodlar
    print("Hata: Sıfıra bölme hatası!")


"""
Bu örnekte, kullanıcıdan bir sayı alarak 10'a bölmeyi deniyoruz. Eğer kullanıcı sıfır girerse ZeroDivisionError hatası oluşur. try bloğunda bu hatanın oluşabileceği kodlar yer alırken, except bloğunda ise bu hatayı ele alacak kodlar bulunur. Eğer hata oluşursa, except bloğu çalışır ve "Hata: Sıfıra bölme hatası!" mesajı ekrana yazdırılır.
"""

# Örnek 2: Birden fazla hata türünü ele almak için try-except kullanımı

try:
    # Potansiyel hata oluşabilecek kodlar
    num1 = int(input("Birinci sayıyı girin: "))
    num2 = int(input("İkinci sayıyı girin: "))
    result = num1 / num2
    print("Sonuç:", result)
except ZeroDivisionError:
    # Sıfıra bölme hatası
    print("Hata: Sıfıra bölme hatası!")
except ValueError:
    # Geçersiz sayı girişi hatası
    print("Hata: Geçersiz sayı girişi!")

"""

Bu örnekte, kullanıcıdan iki sayı alarak birbirine bölmeyi deniyoruz. try bloğunda potansiyel olarak ZeroDivisionError (sıfıra bölme hatası) ve ValueError (geçersiz sayı girişi hatası) oluşabilecek kodlar yer alır. except blokları, bu hata türlerini sırasıyla ele alacak kodları içerir. Eğer bir hata oluşursa, ilgili except bloğu çalışır ve uygun hata mesajı ekrana yazdırılır.

Bu örneklerde gösterilen try-except blokları, programın hata durumlarıyla başa çıkmasını sağlar. Hatalar oluştuğunda programın çökmesini önler ve kullanıcıya uygun hata mesajlarını gösterir. Ayrıca, birden fazla hata türünü ele almak için birden çok except bloğu kullanabiliriz.

"""