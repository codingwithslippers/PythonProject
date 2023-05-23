#Sol sütunda, Personel sinifina ait bir kişinin bulent cobanoglu'nun ad, soyad ve mail bilgilerini ekrana yazdıran bir program yazdık. Fakat bu programda kişi adını doğrudan bir nitelik gibi değiştirmek istediğimizde (kisi1.Ad='bayram aksu şeklinde) başarılı olamadık. Sağ sütunda ise programda bir değişiklik yapmadan sadece dekoratörler kullanarak kişi adını doğrudan değiştirdik.

# Bir örnek uygulama üzerinden  anlattığımız dekoratör kavramını ve @property kullanımı açıklayalım:

# Dekarotörsüz Kullanım:
class Personel:
    def __init__(self, ad, soyad):
        self.ad = ad
        self.soyad = soyad    
    def mail(self):
        return '{}.{}@gmail.com'.format(self.ad, self.soyad)
    def Ad(self):
        return '{} {}'.format(self.ad, self.soyad)
    def Ad(self, isim):
        ad, soyad = isim.split(' ')
        self.ad = ad
        self.soyad = soyad        
kisi1 = Personel('bulent', 'cobanoglu')
kisi1.Ad('bayram aksu') 
print("Ad: ", kisi1.ad) 
print("Soyad: ", kisi1.soyad) 
print("Mail: ", kisi1.mail())
# EKRAN CIKTISI
# Ad: bulent
# Soyad: cobanoglu
# mail: cobanoglubulent@gmail.com

# Dekarotörlü Kullanım:
class Personel:
    def __init__(self, ad, soyad):
        self.ad = ad
        self.soyad = soyad
    
    @property
    def mail(self):
        return '{}.{}@gmail.com'.format(self.ad, self.soyad)
    
    @property
    def Ad(self):
        return '{} {}'.format(self.ad, self.soyad)
    
    @Ad.setter
    def Ad(self, isim):
        ad, soyad = isim.split(' ')
        self.ad = ad
        self.soyad = soyad   
kisi1 = Personel('bulent', 'cobanoglu')
kisi1.Ad = 'bayram aksu'
print("Ad: ", kisi1.ad)
print("Soyad: ", kisi1.soyad)
print("Mail: ", kisi1.mail)
# EKRAN CIKTISI
# Ad: bayram
# Soyad:aksu 
# mail: aksubayram@gmail.com
