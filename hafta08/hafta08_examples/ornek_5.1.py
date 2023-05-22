# Sayılardan oluşan sırasız bir A=(2, 3, 5, 8, 9, 12, 34, 6, 77) demetinde aranan sayı varsa sayının yerini, sırası ile birlikte bulan programı kodlayınız.

A = (2, 3, 5, 8, 9, 12, 34, 6, 77)
aranan = int(input("Aramak istediğiniz sayıyı girin: "))

if aranan in A:
    index = A.index(aranan)
    sirasi = index + 1
    print(f"{aranan} sayısı, demette {sirasi}. sırada bulunuyor.")
else:
    print(f"{aranan} sayısı demette bulunamadı.")

# Ekran Çıktısı 
# Aramak istediğiniz sayıyı girin:13
# 13 sayısı demette bulunamadı.

# Aramak istediğiniz sayıyı girin:5
# 5 sayısı, demette 3.sırada bulunuyor.

