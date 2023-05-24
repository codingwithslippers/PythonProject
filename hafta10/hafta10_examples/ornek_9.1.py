class myHatam(Exception):
    def __init__(self, mesaj):
        self.mesaj = mesaj

try:
    sayi = int(input("Bir sayı girin: "))
    if sayi < 0:
        raise myHatam("Negatif sayı girişi yapılamaz.")
    else:
        print("Girilen sayı:", sayi)
except myHatam as hata:
    print("Hata oluştu:", hata.mesaj)
except ValueError:
    print("Geçersiz sayı girişi.")
finally:
    print("Program sonlandırılıyor.")


