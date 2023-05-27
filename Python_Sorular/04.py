# Kurallar

# Sağlanan kod taslağı STDIN'den a ve b olmak üzere iki tamsayı okur.

# İlk satır tamsayı bölme işleminin sonucunu içermelidir, a // b.


# İkinci satır float bölme işleminin sonucunu içermelidir, a/b.

# Yuvarlama veya biçimlendirme gerekmez.


# Örnek 1
# a = 3
# b = 5


# Örnek 1 Ekran Çıktıları
# 0
# 0.6


# Yukarıdaki verilen kurallara göre kodlayınız.

a = int(input())
b = int(input())

tam_bolum = a // b
float_bolum = a / b

print(tam_bolum)
print(float_bolum)

