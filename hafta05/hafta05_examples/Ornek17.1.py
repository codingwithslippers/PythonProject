count = 0 # asal sayı sayacı

# 2 de dahil olmak üzere ilk 100 sayı arasında döngü
for num in range(2, 101):
    # asal sayı kontrolü
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        count += 1
        print(num, end=" ")

# asal sayı adedini yazdırma
print("\nAsal Sayı Adedi:", count)


