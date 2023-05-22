kupur=[200, 100, 50, 20, 10, 5, 1, 0.5, 0.25, 0.10, 0.05]
para= float(input('Para Miktarınızı Giriniz..:'))
for i in range(11):
    sayi=float(para)//kupur[i]
    if sayi !=0:
        print(sayi , 'TL', 'adet',kupur[i])
    para= para-sayi*kupur[i]



