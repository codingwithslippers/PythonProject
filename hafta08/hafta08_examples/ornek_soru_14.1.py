# İllerin hava durumunu bir sözlükte tutan ve ekranda alt alta listeleyen programı yazınız.
hava_durumu = {
    "Ankara": "Güneşli",
    "İstanbul": "Parçalı Bulutlu",
    "İzmir": "Yağmurlu",
    "Antalya": "Sisli",
    "Bursa": "Karlı"
}

print("İllerin Hava Durumu")
print("-------------------")
for il, durum in hava_durumu.items():
    print(f"{il}: {durum}")


# Ekran Çıktısı
# İllerin Hava Durumu
# -------------------
# Ankara: Güneşli
# İstanbul: Parçalı Bulutlu
# İzmir: Yağmurlu
# Antalya: Sisli
# Bursa: Karlı




