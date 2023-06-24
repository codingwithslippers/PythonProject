# Verilen bir sayının faktöriyelini hesaplayan bir Python fonksiyonu nasıl yazılır?

def faktoriyel(sayi):
    if sayi == 0:
        return 1
    else:
        return sayi * faktoriyel(sayi - 1)

# Örnek kullanım
sayi = 5
print(faktoriyel(sayi))
