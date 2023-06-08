# Kullanıcıdan alınan iki sayıyla toplama, çıkarma, çarpma ve bölme işlemlerini yapan basit bir hesap makinesi Python kodu kodlayiniz.

sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

print("İşlem Seçin:")
print("1 - Toplama")
print("2 - Çıkarma")
print("3 - Çarpma")
print("4 - Bölme")

secim = input("İşlem numarasını girin (1/2/3/4): ")

if secim == "1":
    sonuc = sayi1 + sayi2
    print("Sonuç:", sonuc)
elif secim == "2":
    sonuc = sayi1 - sayi2
    print("Sonuç:", sonuc)
elif secim == "3":
    sonuc = sayi1 * sayi2
    print("Sonuç:", sonuc)
elif secim == "4":
    if sayi2 != 0:
        sonuc = sayi1 / sayi2
        print("Sonuç:", sonuc)
    else:
        print("Bölme işlemi için ikinci sayı sıfır olamaz!")
else:
    print("Geçersiz işlem numarası!")
