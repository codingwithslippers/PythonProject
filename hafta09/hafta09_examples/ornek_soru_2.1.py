# Bir sınıfın nasıl tanımlanacağını, bu sınıftan nasıl nesneler türetileceğini ve türetilen nesnelere nasıl cağrı yapılacağını bir araba örneği ile açıklayınız.

# ÇÖZÜM AÇIKLAMASI
# Bu örnekte; 4 parametreli (model, renk, motor, kapasite) bir Araba sınıfı oluşturduk. Bu Araba sınıfından kamyon ve taksi nesnelerini ürettik. Ekran çıktısını __str__() metodu içerisinde ayarladık.

class Araba:
    def __init__(self, model, renk, motor, kapasite):
        self.model = model
        self.renk = renk
        self.motor = motor
        self.kapasite = kapasite

    def __str__(self):
        return f"Model: {self.model}\nRenk: {self.renk}\nMotor: {self.motor}\nKapasite: {self.kapasite}"



kamyon = Araba("MAN", "Siyah", "Diesel", "5000 kg")
taksi = Araba("Toyota", "Sarı", "Benzin", "4 kişi")

print(kamyon)
print()
print(taksi)

# EKRAN ÇIKTILARI
# Model: MAN
# Renk: Siyah
# Motor: Diesel
# Kapasite: 5000 kg
# 
# Model: Toyota
# Renk: Sarı
# Motor: Benzin
# Kapasite: 4 kişi

