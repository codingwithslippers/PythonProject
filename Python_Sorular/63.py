# Verilen bir listedeki tek sayıların karelerinin toplamını ve çift sayıların küplerinin toplamını bulan bir programı nasıl yazarsınız?


def calculate_sum_of_squares_and_cubes(numbers):
    sum_of_squares = 0
    sum_of_cubes = 0

    for num in numbers:
        if num % 2 == 0:  # Çift sayı
            sum_of_cubes += num ** 3
        else:  # Tek sayı
            sum_of_squares += num ** 2

    return sum_of_squares, sum_of_cubes

# Örnek kullanım
numbers = [1, 2, 3, 4, 5, 6]
sum_of_squares, sum_of_cubes = calculate_sum_of_squares_and_cubes(numbers)
print("Tek sayıların kareleri toplamı:", sum_of_squares)
print("Çift sayıların küpleri toplamı:", sum_of_cubes)


"""
Bu program, verilen listedeki tek sayıların karelerinin toplamını ve çift sayıların küplerinin toplamını hesaplar. Programda, for döngüsü kullanarak listenin her bir elemanını kontrol ederiz. Eğer sayı çift ise (num % 2 == 0), o sayının küpünü (num ** 3) çift sayıların küpleri toplamına ekleriz. Eğer sayı tek ise, o sayının karesini (num ** 2) tek sayıların kareleri toplamına ekleriz.

Yukarıdaki örnekte, verilen listedeki tek sayıların karelerinin toplamı ve çift sayıların küplerinin toplamı hesaplanır ve ekrana yazdırılır:
"""

"""EKRAN CIKTISI

Tek sayıların kareleri toplamı: 35
Çift sayıların küpleri toplamı: 288

"""