# Kullanıcıdan alınan dört kenarın bilgisine göre şeklin kare,dikdörtgen veya diğer dörtgenlerden olduğunu belirten kodu yazınız.

a = int(input("1. kenar: "))
b = int(input("2. kenar: "))
c = int(input("3. kenar: "))
d = int(input("4. kenar: "))

if a == b == c == d:
    print("Kare!")
elif a == c and b == d:
    print("Dikdörtgen!")
else:
    print("Diğer Dörtgen!")
