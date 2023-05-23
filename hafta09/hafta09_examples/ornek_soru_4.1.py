class Araba:
    def __init__(self, hiz, renk, durum):
        self.hiz = hiz
        self.renk = renk
        self.durum = durum
    def __str__(self):
        return "Hız: {}\nRenk: {}\nDurum: {}".format(self.hiz, self.renk, self.durum)
    def calis(self):
        print("Çalışıyor...")
    def dur(self):
        print("Duruyor...")
class Kamyon(Araba):
    def __init__(self, hiz, renk, durum, kn):
        super().__init__(hiz, renk, durum)
        self.kn = kn
    def __str__(self):
        return super().__str__() + "\nKasa Numarası: {}".format(self.kn)
class Taksi(Araba):
    def __init__(self, hiz, renk, durum, km):
        super().__init__(hiz, renk, durum)
        self.km = km
    def __str__(self):
        return super().__str__() + "\nKilometre: {}".format(self.km)
def test():
    k = Kamyon(70, "kırmızı", False, 123)
    print(k)
    k.dur()
    t = Taksi(90, "sarı", True, 54000)
    print(t)
    t.calis()
if __name__ == "__main__":
    test()
# Hız: 70
# Renk: kırmızı
# Durum: False
# Kasa Numarası: 123
# Duruyor...
# Hız: 90
# Renk: sarı
# Durum: True
# Kilometre: 54000
# Çalışıyor...
