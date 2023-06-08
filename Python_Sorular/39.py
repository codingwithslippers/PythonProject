# Beden kütle endeksi kilo/boy^2 formülü ile hesaplanarak bireyin kilolu normal zayıf veya obez sınıfına girdiği ile ilgili sonuç verir. Kütle Endeksi (KE) < 18.5 ise Zayıf , 18.5 < (KE) <=25 ise Normal , 25 < (KE) <= 30 ise Kilolu , (KE) > 25 ise birey obez sınıfına girmektedir. Kütle endeksi kodunu yazınız.

boy = float(input("Boy:"))
kilo = int(input("Kilo:"))

endeks  = kilo/(boy**2)

if endeks<18.5:
    print("n Zayıf")
elif endeks > 18.5 and endeks <=25 :
    print("n Normal")
elif endeks > 25 and endeks <=30:
    print("n Kilolu")
elif endeks > 30:
    print("n Obez")