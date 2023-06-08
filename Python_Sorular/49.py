# Permütasyon nesnelerin diziliş sayısını bulmamızı sağlar. 6 arkadaştan 4’ü masaya oturucaktır. Bu 4 kişi kaç farklı şekilde masaya oturabilir sorusuna çözüm bulmak için permütasyon kullanırız. Aldığı sayılara göre permütasyon hesabı yapan kodu yazınız.

import math

nesne_sayisi = int(input("Nesne sayısını girin: "))
dizilecek_sayi = int(input("Dizilecek nesne sayısını girin: "))

if nesne_sayisi < dizilecek_sayi:
    print("Hatalı giriş! Dizilecek nesne sayısı, nesne sayısından büyük olamaz.")
else:
    permütasyon = math.perm(nesne_sayisi, dizilecek_sayi)
    print("Permütasyon:", permütasyon)
