# İsim ve Soy isimleri atadığınız listeden rastgele isim ve soy isimler seçerek isim oluşturan Python kodunu yazınız.

import random

isimler = ["Ali", "Ayşe", "Mehmet", "Fatma", "Ahmet", "Zeynep", "Mustafa", "Emine", "Hasan", "Hülya"]
soyisimler = ["Yılmaz", "Kaya", "Demir", "Çelik", "Aksoy", "Öztürk", "Çetin", "Aydın", "Taş", "Şahin"]

random_isim = random.choice(isimler)
random_soyisim = random.choice(soyisimler)

olusan_isim = random_isim + " " + random_soyisim
print("Oluşan İsim: ", olusan_isim)


