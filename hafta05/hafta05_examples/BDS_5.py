s1 = int(input("Lütfen birinci sayıyı girin: "))
s2 = int(input("Lütfen ikinci sayıyı girin: "))

if s1 > s2:
    s1, s2 = s2, s1

for i in range(s1, s2+1):
    if i % 2 != 0:
        print(i)


