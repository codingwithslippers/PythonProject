# Örnek Soru 1.1: Bir araba sınıfından ‘Kamyon’, ‘Taksi’ nesnelerini oluşturup, bazı özelliklerini ekrana yazdıran uygulamayı farklı şekilde kodlayınız.



# Çözüm
# Bir sınıftan (Araba) aynı anda, birbirinden bağımsız çok sayıda (kmayon, taksi,...) nesneleri üretilebilir.

class Araba():
    # Sınıf Özellikleri
    model='MAN'
    renk='Kırmızı'
    kapasite='25000'
    silindir='6'

kamyon=Araba()
taksi=Araba()
taksi.model='Renault Clio'
taksi.silindir='4'
print('kamyon modeli..:', kamyon.model)
print('taksi  modeli..:', taksi.model)

# EKRAN ÇIKTISI
# kamyon modeli..: MAN
# taksi  modeli..: Renault Clio


