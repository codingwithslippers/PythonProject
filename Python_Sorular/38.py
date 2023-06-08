# Dik üçgende dik açının karşısındaki kenara hipotenüs denir. Hipotenüs formülü : a^2 + b^2 = c^2 olduğuna göre kullanıcıdan alınan A ve B kenarına göre hipotenüsü hesaplayan Python kodu yazınız.

a = int(input("A:"))
b = int(input("B:"))

c = (a ** 2 + b ** 2) ** 0.5

print("nHipotenüs:",c)