#  Verilen bir sayının Armstrong sayı olup olmadığını kontrol eden bir programı nasıl yazarsınız?

"""
Armstrong sayısı, bir sayının basamaklarındaki rakamların küplerinin toplamı, sayının kendisine eşit olduğunda oluşur. Örneğin, 153 sayısı bir Armstrong sayısıdır çünkü 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.

Bir sayının Armstrong sayı olup olmadığını kontrol eden bir programı aşağıdaki gibi yazabilirsiniz:
"""


def is_armstrong_number(number):
    # Sayıyı stringe çevirerek basamaklarına ayırma
    digits = str(number)

    # Basamak sayısını bulma
    num_digits = len(digits)

    # Rakamların küplerini toplama
    total = sum(int(digit) ** num_digits for digit in digits)

    # Toplamın, sayıya eşit olup olmadığını kontrol etme
    if total == number:
        return True
    else:
        return False


# Örnek kullanım
number = 153
if is_armstrong_number(number):
    print(number, "bir Armstrong sayısıdır.")
else:
    print(number, "bir Armstrong sayısı değildir.")




"""Bu program, verilen sayının Armstrong sayı olup olmadığını kontrol etmek için aşağıdaki adımları izler:

1-Sayıyı stringe çevirerek basamaklarına ayırırız.
2-Basamak sayısını buluruz.
3-Her bir basamağı küpünü alarak toplamı hesaplarız.
4-Toplamın, sayıya eşit olup olmadığını kontrol ederiz.


Yukarıdaki örnekte, 153 sayısının Armstrong sayı olduğunu kontrol ediyoruz. Eğer sayı Armstrong sayıysa, "bir Armstrong sayısıdır" mesajını yazdırırız. Aksi takdirde, "bir Armstrong sayısı değildir" mesajını yazdırırız. Programın çıktısı "153 bir Armstrong sayısıdır" olacaktır.
"""