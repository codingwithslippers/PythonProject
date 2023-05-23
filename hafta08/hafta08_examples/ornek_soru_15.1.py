# Girilen İngilizce günün Türkçe karşılığını veren İngilizce-Türkçe bir sözlük programı yazınız.
gunler = {
    "Monday": "Pazartesi",
    "Tuesday": "Salı",
    "Wednesday": "Çarşamba",
    "Thursday": "Perşembe",
    "Friday": "Cuma",
    "Saturday": "Cumartesi",
    "Sunday": "Pazar"
}

ingilizce_gun = input("Bir İngilizce gün girin: ")

turkce_gun = gunler.get(ingilizce_gun)

if turkce_gun:
    print("Türkçe karşılığı:", turkce_gun)
else:
    print("Girdiğiniz gün bulunamadı.")

# EKRAN ÇIKTILARI
# Bir İngilizce gün girin: Tuesday
# Türkçe karşılığı: Salı

# Bir İngilizce gün girin: Testday
# Girdiğiniz gün bulunamadı.


