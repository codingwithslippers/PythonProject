# Kullanıcıdan ismini alarak harflere ayıran ve bu harflerle başlayan şehirleri sırasıyla ekrana yazdıran kodu yazınız. ( Ğ , Ü gibi harfler için farklı bir bilgi yazdırabilirsiniz. )

isim = input("İsminizi girin: ")
harfler = list(isim.lower())

sehirler = [
    "Adana", "Adıyaman", "Afyonkarahisar", "Ağrı", "Amasya", "Ankara", "Antalya", "Artvin", "Aydın",
    "Balıkesir", "Bilecik", "Bingöl", "Bitlis", "Bolu", "Burdur", "Bursa",
    "Çanakkale", "Çankırı", "Çorum",
    "Denizli", "Diyarbakır", "Düzce",
    "Edirne", "Elazığ", "Erzincan", "Erzurum", "Eskişehir",
    "Gaziantep", "Giresun", "Gümüşhane",
    "Hakkari", "Hatay",
    "Iğdır", "Isparta", "İçel", "İstanbul", "İzmir",
    "Kahramanmaraş", "Karabük", "Karaman", "Kars", "Kastamonu", "Kayseri", "Kırıkkale", "Kırklareli", "Kırşehir", "Kilis", "Kocaeli", "Konya", "Kütahya",
    "Malatya", "Manisa", "Mardin", "Mersin", "Muğla", "Muş",
    "Nevşehir", "Niğde",
    "Ordu", "Osmaniye",
    "Rize",
    "Sakarya", "Samsun", "Siirt", "Sinop", "Sivas",
    "Şanlıurfa",
    "Şırnak",
    "Tekirdağ", "Tokat", "Trabzon", "Tunceli",
    "Uşak",
    "Van",
    "Yalova", "Yozgat",
    "Zonguldak"
]

baslayan_sehirler = []

for harf in harfler:
    sehir_bulundu = False
    for sehir in sehirler:
        if sehir.lower().startswith(harf):
            baslayan_sehirler.append(sehir)
            sehir_bulundu = True
    if not sehir_bulundu:
        baslayan_sehirler.append("Şehir bulunamadı: " + harf.upper())

for sehir in baslayan_sehirler:
    print(sehir)
