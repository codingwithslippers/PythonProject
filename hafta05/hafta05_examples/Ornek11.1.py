yeniS1 = 1
yeniS2 = 1

eskiS=0 ; sayac = 0

print ('Fibonacci Serisi......:')
while True:
    print(yeniS2)
    yeniS2 = eskiS + yeniS1
    eskiS = yeniS1
    yeniS1 = yeniS2
    sayac = sayac + 1
    if sayac == 13 : break

print ( 'Altın Oran.:', yeniS1/yeniS2)



