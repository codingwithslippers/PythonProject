L = ["Ocak","Şubat","Mart","Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık",]
ay=int(input('Kaçıncı ay..:'))
if ay>0 and ay<=12:
    print(ay,".ay..:" + L[ay-1])
else:
    print("Hatalı giriş gerçekleştirdiniz!")


# Ekran Çıktısı
# Kaçıncı ay..:6
# 6 .ay..:Haziran


