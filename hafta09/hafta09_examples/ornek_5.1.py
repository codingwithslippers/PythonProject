class TV:
    # setter fonksiyonları
    def setUz(self, u):
        self.boy = u

    def setEn(self, e):
        self.en = e

    # getter fonksiyonu
    def getSes(self):
        return self.boy * self.en
# Ana Program
nesne = TV()
nesne.setUz(10.0)
nesne.setEn(8.0)
print("Ses Ayarı:", nesne.getSes())
print("Erişim:", dir(nesne))
# Ekran Çıktısı
# Ses Ayarı: 80.0
 #Erişim: ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'boy', 'en', 'getSes', 'setEn', 'setUz']


