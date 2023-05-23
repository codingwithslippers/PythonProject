# 19 yapraklı ‘Seviyor/Sevmiyor' elemanlarından oluşan bir papatya listesinden papatya falı çeken uygulamayı gerçekleştiriniz. {Not: Elemanlar kümeden rastgele çekilecektir.}

# SÖZLÜK YAPISI İLE ÇÖZÜM
#------------------------

Fal= {1:"Seviyor", 2:"Sevmiyor",3:"Seviyor", 4:"Sevmiyor",5:"Seviyor", 6:"Sevmiyor",7:"Seviyor", 8:"Sevmiyor",9:"Seviyor", 10:"Sevmiyor",11:"Seviyor", 12:"Sevmiyor",13:"Seviyor", 14:"Sevmiyor",15:"Seviyor", 16:"Sevmiyor",17:"Seviyor", 18:"Sevmiyor",19:"Seviyor"}

for i in range(1,len(Fal)):
    Fal.popitem()
    print(Fal)

# LİSTE  YAPISI İLE ÇÖZÜM
#------------------------

import random

Fal=["Seviyor", "Sevmiyor","Seviyor", "Sevmiyor","Seviyor", "Sevmiyor","Seviyor", "Sevmiyor","Seviyor", "Sevmiyor","Seviyor", "Sevmiyor","Seviyor", "Sevmiyor","Seviyor", "Sevmiyor","Seviyor", "Sevmiyor","Seviyor"]
for i in range(0, 18):
    x = random.randint(0, 1)
    Fal.pop(x)
    print(Fal)



# LİSTE  YAPISI İLE ÇÖZÜM-2
#--------------------------
import random

papatya = ["Seviyor", "Sevmiyor"]  # Papatya yapraklarının listesi

def papatya_fali():
    fal = random.choice(papatya)  # Rastgele bir yaprak seçilir
    return fal

print("Papatya Falı Çekiliyor...")
print("Sonuç:", papatya_fali())


