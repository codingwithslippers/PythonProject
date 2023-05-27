# Takvime neredeyse her dört yılda bir 29 Şubat olarak fazladan bir gün eklenir ve bu güne artık gün adı verilir. Takvim, gezegenimizin güneş etrafındaki yörüngesinin yaklaşık 365,25 gün sürdüğü gerçeğine göre düzeltilir. Artık yıl bir artık gün içerir.

# Gregoryen takviminde artık yılları belirlemek için üç koşul kullanılır:
# 1- The year can be evenly divided by 4, is a leap year, unless:
    # 2- The year can be evenly divided by 100, it is NOT a leap year, unless:
        # 3- The year is also evenly divisible by 400. Then it is a leap year.

# Bu, Gregoryen takviminde 2000 ve 2400 yıllarının artık yıl olduğu, 1800, 1900, 2100, 2200, 2300 ve 2500 yıllarının ise artık yıl olmadığı anlamına gelmektedir.(https://www.timeanddate.com/date/leapyear.html)

# Kurallar

# Bir yıl verildiğinde, artık yıl olup olmadığını belirleyin.
# Artık yıl ise Boolean True döndürür, aksi takdirde False döndürüren fonksiyonu programlayınız.


# Örnek 1
# 1990

# Örnek 1 Çıktı
# False


def artik_yil_hesapla(yil):
    if yil % 4 == 0:
        if yil % 100 == 0:
            if yil % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Kullanıcıdan yıl girmesini isteyelim
yil = int(input("Bir yıl girin: "))

if artik_yil_hesapla(yil):
    print(yil, "bir artık yıldır.")
else:
    print(yil, "bir artık yıl değildir.")

