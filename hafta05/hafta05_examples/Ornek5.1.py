Sayac = 0
T = 0
N = int (input('Bir sayı giriniz.:'))
X = N - (N % 3)
while X > 0:
    T = T + X
    X = X - 3
    Sayac = Sayac + 1

Ort = T / Sayac
print('Ortalama =', Ort)


