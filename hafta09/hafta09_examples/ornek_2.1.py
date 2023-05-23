# ÇÖZÜM-1
class Han ():
    def __init__(self):
        self.zar =1
        self.zar =2
        self.zar =3
a = Han()
print(a.zar)   #1
print(a._zar)  #2
print(a.__zar) #Attribute Error
# EKRAN ÇIKTISI
# AÇIKLAMA
# BİR SINIF ÜYESİNİN (ZAR) ÖNÜNDE TEK ALT TİRE '_' OLMASI İLE HİÇ ALT TİRE OLMAMASI ARASINDA PRATİKTE BİR FARK YOKTUR. PRIVATE  ÜYEYE İSE DOĞRUDAN 'a.__zar' ŞEKLİNDE ERİŞİM MÜMKÜN DEĞİLDİR.

# ÇÖZÜM-2
class Han ():
    def __init__(self):
        self.zar=1
        self._zar=2
        self.__zar=3
a = Han()
print(a._Han__zar)#3
print(Han().__dict__)
# EKRAN ÇIKTISI
# AÇIKLAMA
# Private bir sınıf üyesi dolaylı olarak, 'a._Han__zar (nesne._Sınıf__Üye)' şeklinde erişebilirsiniz. Bir sınıf üyesinin tüm değerlerini erişim belirteçleri ile birlikte bir sözlük (dict) yapısı şeklinde {} içerisinde elde etmek için __dict__ metodunu kullandık.

