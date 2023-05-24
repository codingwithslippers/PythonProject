try:
    dosya = open("dosya.txt", "r")
    try:
        # Dosyadaki verileri işleme
        for satir in dosya:
            print(satir.strip())
    finally:
        dosya.close()
        print("Dosya kapatıldı.")
except FileNotFoundError:
    print("Dosya bulunamadı.")
except:
    print("Bir hata oluştu.")
finally:
    print("Program sonlandırılıyor.")



