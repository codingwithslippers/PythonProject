while True:
    try:
        sayi = int(input("Bir sayı girin: "))
        kare = sayi ** 2
        print("Girdiğiniz sayının karesi:", kare)
        break  # Hata oluşmadığı durumda döngüyü sonlandır
    except ValueError:
        print("Hatalı giriş yaptınız. Lütfen bir sayı girin.")


