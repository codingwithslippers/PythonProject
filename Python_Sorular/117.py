# Verilen iki dizinin kesişim elemanlarını bulan bir Python fonksiyonu nasıl yazılır?

def kesisim(dizi1, dizi2):
    kesisim_elemanlari = set(dizi1) & set(dizi2)
    return list(kesisim_elemanlari)

# Örnek kullanım
dizi1 = [1, 2, 3, 4, 5]
dizi2 = [4, 5, 6, 7, 8]
print(kesisim(dizi1, dizi2))
