# Sağlanan kod taslağı STDIN'den n tamsayısını okur.
# Negatif olmayan tüm i < n tamsayıları için i**2 yazdırır.


# Örnek 1
# n = 3

# n=3'ten küçük olan negatif olmayan tam sayıların listesi [1,2,3]'tür.
# Her sayının karesini ayrı bir satıra yazdırın.

# Örnek 1 Ekran Çıktısı
# 0
# 1
# 4

n = int(input())

for i in range(n):
    print(i**2)
