L=[]
T=0

for i in range(24):
    if i%2==0:
        L.append(i)
        T=T+i
        print(L)
print("Toplam=", T)
# Ekran Çıktısı
# [0]
# [0, 2]
# [0, 2, 4]
# [0, 2, 4, 6]
# [0, 2, 4, 6, 8]
# [0, 2, 4, 6, 8, 10]
# [0, 2, 4, 6, 8, 10, 12]
# [0, 2, 4, 6, 8, 10, 12, 14]
# [0, 2, 4, 6, 8, 10, 12, 14, 16]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]
# Toplam= 132



