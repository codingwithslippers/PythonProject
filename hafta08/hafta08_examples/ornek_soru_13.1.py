# İl plakalarını tutan bir sözlük yapısı oluşturarak sözlüğe eleman ekleme ve sorgulamanın nasıl yapılacağını gösteren bir program yazınız.

plaka_sozlugu = {}  # Boş bir sözlük oluşturuluyor

# Sözlüğe eleman ekleme
plaka_sozlugu["Ankara"] = 6
plaka_sozlugu["İstanbul"] = 34
plaka_sozlugu["İzmir"] = 35
plaka_sozlugu["Antalya"] = 7
plaka_sozlugu["Bursa"] = 16

# Sözlükteki elemanları sorgulama
sehir = input("Plakasını öğrenmek istediğiniz şehri girin: ")
if sehir in plaka_sozlugu:
    plaka = plaka_sozlugu[sehir]
    print(f"{sehir} şehrinin plakası: {plaka}")
else:
    print("Bu şehir sözlükte bulunmamaktadır.")

# Plakasını öğrenmek istediğiniz şehri girin: İzmir
# İzmir şehrinin plakası: 35




