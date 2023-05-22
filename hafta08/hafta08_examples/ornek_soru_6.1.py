A = []
B = []

# Asal sayı bulan program
def isAsal(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for n in range(0, 35):
    if isAsal(n):
        A.append(n)
    else:
        B.append(n)

print("Asal Sayı Olanlar:", A)
print("Asal Sayı Olmayanlar:", B)

# Ekran Çıktıları
# Asal Sayı Olanlar: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
# Asal Sayı Olmayanlar: [0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34] 





