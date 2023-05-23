from abc import ABC, abstractmethod

class ustSinif(ABC):
    @abstractmethod
    def soyutMetot(self):
        pass

class altSinif(ustSinif):
    def soyutMetot(self):
        # Soyut metotun uygulamasını burada yapın
        pass

'''Yukarıdaki örnekte abc modülünden ABC sınıfını ve abstractmethod dekoratörünü import ettik. ustSinif adında bir üst sınıf oluşturduk ve ABC sınıfından türetildiğini belirtmek için parantez içinde ABC sınıfını belirttik.

soyutMetot adında bir soyut metot tanımladık ve @abstractmethod dekoratörünü kullanarak bu metodu soyut hale getirdik. Soyut metotlar alt sınıflar tarafından uygulanması gereken metotlardır.

Son olarak altSinif adında bir alt sınıf oluşturduk ve ustSinif sınıfından türettiğimizi belirttik. Alt sınıfta soyutMetot metodunu uygulayarak soyut metodu gerçek bir işlevsellikle doldurabilirsiniz.
'''

