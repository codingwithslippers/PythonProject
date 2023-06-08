# Kullanıcıdan alınan iki sayı arasındaki asal sayıları bulan Python kodunu yazınız.


def is_asal(sayi):
    if sayi < 2:
        return False
    for i in range(2, int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            return False
    return True

baslangic = int(input("Başlangıç sayısını girin: "))
bitis = int(input("Bitiş sayısını girin: "))

print("Asal sayılar:")
for sayi in range(baslangic, bitis + 1):
    if is_asal(sayi):
        print(sayi)
