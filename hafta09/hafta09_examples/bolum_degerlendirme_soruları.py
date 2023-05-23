#1
# Sınıf ile nesne arasındaki fark nedir?

# Sınıf, bir nesnenin özelliklerini ve davranışlarını tanımlayan bir yapıdır.
# Sınıf, bir şablondur ve nesnelerin oluşturulmasını sağlar.
# Sınıflar, benzer özelliklere ve davranışlara sahip nesneleri gruplamak için kullanılır.

# Nesne, bir sınıftan türetilen bir örnek veya bir sınıfın bir örneğidir.
# Nesne, sınıf tarafından tanımlanan özelliklere (nitelikler veya öznitelikler) ve davranışlara (metodlar) sahip olur.
# Sınıftan türetilen her bir nesne, kendi özgün özelliklere sahip olabilir.

# Özetle, sınıf, bir nesnenin şablonunu tanımlayan yapılardır.
# Nesne ise bir sınıfın bir örneğidir ve sınıftan türetilerek özelliklere ve davranışlara sahip olur.
# Sınıflar nesnelerin oluşturulmasını sağlar ve nesneler sınıfın tanımladığı özellikleri taşır.
#2 
class Ulke():
    def Memleket(self):
        print("TURKIYE")

class Test(Ulke):
    def Memleket(self):
        print("ERZINCAN")

# Ana program
t2 = Ulke()
t1 = Test()
t2.Memleket()
t1.Memleket()
# CIKTI
# TURKIYE
# ERZINCAN

#3 Bir sınıf üyesine 'private' erişim belirteci özelliği (yani gizlilik) kazandırmak için ne yapılmalıdır?
# Cevap: Üye adının başına çift alt çizgi (__) eklenmelidir. Örneğin, private bir değişken için `_private_variable` şeklinde isimlendirme yapabilirsiniz.

#4 Pythonda soyut sınıf (abstract base classes) tanımlamak için hangi modül kullanılır?
# Cevap: Pythonda soyut sınıflar (abstract base classes) tanımlamak için `abc` modülü kullanılır. `from abc import ABC, abstractmethod` ifadesiyle bu modül içindeki `ABC` sınıfı ve `abstractmethod` dekoratörü kullanılarak soyut sınıflar tanımlanabilir.

#5 Python'da, bir sınıftan bir örnek (nesne) oluşturulduğunda ilk olarak otomatik yapılandırıcı metot çağrılır. Bu metodun ismi nedir?
# Cevap: Bu metoda 'otomatik yapılandırıcı metot' veya 'yapılandırıcı metot' denir. İsmi `__init__` olarak tanımlanır.

#6 Sınıf içerisinden erişilecek üyeler için kullanılır. Nesnenin kendisini referans etmesini sağlar. Başka bir ifade ile sözü edilen nesneyi doğrudan göstermek için kullanılır. Java dilindeki this deyimi ile benzer işleve sahip olan bu Python deyiminin ismi nedir?
# Cevap: Bu Python deyimi `self` olarak adlandırılır. `self`, sınıf içindeki metotlarda kullanılarak o metoda ait nesneye erişmeyi sağlar.
