
#Normal fonksiyon ile faktöriyel hesaplama:

def faktoriyel(n):
    fakt = 1
    for i in range(1, n+1):
        fakt *= i
    return fakt

sayi = 5
print(f"{sayi} sayısının faktöriyeli: {faktoriyel(sayi)}")

'''

Bu örnekte, faktoriyel() adlı bir fonksiyon tanımlanmıştır. Fonksiyon, n sayısının faktöriyelini hesaplamak için döngü kullanır. Başlangıçta fakt değişkeni 1 olarak atanır ve ardışık olarak 1'den n'e kadar olan sayıları çarparak faktöriyel değerini hesaplar.

'''





#Özyinelemeli fonksiyon ile faktöriyel hesaplama:

def faktoriyel(n):
    if n == 0:
        return 1
    else:
        return n * faktoriyel(n-1)

sayi = 5
print(f"{sayi} sayısının faktöriyeli: {faktoriyel(sayi)}")


'''

Bu örnekte, faktoriyel() adlı bir özyinelemeli fonksiyon kullanılmıştır. Fonksiyon, n sayısının faktöriyelini hesaplamak için kendisini tekrar çağırır. Temel durumda (n == 0), fonksiyon 1 değerini döndürür. Özyineleme durumunda ise fonksiyon, n sayısını kendisi ile (n * faktoriyel(n-1)) çarparak faktöriyel değerini hesaplar.

Her iki örnekte de sayi değişkenine 5 atanmıştır ve hesaplanan faktöriyel değeri ekrana yazdırılmıştır. Sonuç olarak, 5 sayısının faktöriyeli olan 120 görüntülenir.

'''

