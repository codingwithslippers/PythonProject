# Kombinasyon hesabı yapan python kodunu yazınız.

import math

nesne_sayisi = int(input("Nesne sayısını girin: "))
secilecek_sayi = int(input("Seçilecek nesne sayısını girin: "))

if nesne_sayisi < secilecek_sayi:
    print("Hatalı giriş! Seçilecek nesne sayısı, nesne sayısından büyük olamaz.")
else:
    kombinasyon = math.comb(nesne_sayisi, secilecek_sayi)
    print("Kombinasyon:", kombinasyon)
