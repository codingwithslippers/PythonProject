a = int(input("Bölünen sayıyı girin: "))
b = int(input("Bölen sayıyı girin: "))

if a < b:
    print("Hatalı giriş! Bölünen sayı, bölen sayıdan büyük olmalıdır.")
else:
    kalan = a
    sayac = 0
    while kalan >= b:
        kalan -= b
        sayac += 1
    print(f"{a} / {b} = {sayac}")


