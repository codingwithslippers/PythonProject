def en_buyuk_kucuk(sayi1, sayi2, sayi3):
    en_buyuk = max(sayi1, sayi2, sayi3)
    en_kucuk = min(sayi1, sayi2, sayi3)
    print("En büyük sayı:", en_buyuk)
    print("En küçük sayı:", en_kucuk)

# Kullanıcıdan üç sayıyı alın
sayi1 = int(input("Birinci sayıyı girin: "))
sayi2 = int(input("İkinci sayıyı girin: "))
sayi3 = int(input("Üçüncü sayıyı girin: "))

# en_buyuk_kucuk fonksiyonunu çağırın
en_buyuk_kucuk(sayi1, sayi2, sayi3)

# ekran çıktısı Birinci sayıyı girin: 5
#İkinci sayıyı girin: 2
#Üçüncü sayıyı girin: 9
#En büyük sayı: 9
#En küçük sayı: 2





