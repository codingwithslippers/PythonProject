# Kutallar

 # Bir tamsayı, n, verildiğinde aşağıdaki koşullu eylemleri gerçekleştirin:
 # 1- Eğer n tek ise, Garip, yazdır
 # 2- n çift ve 5'in 2'si dahil aralığındaysa, Garip Değil, yazdırın
 # 3- n çift ise ve 6 ile 20 arasında bir aralıktaysa Garip, yazdırın
 # 4- n çift ve 20'den büyükse, Garip Değil, yazdırın

# Kısıtlamalar 
#  1 <= n <= 100


# Örnek Girdi 1
# 3

# Örnek Çıktı 1
# Weird

# Örnek Girdi 2
# 24

# Örnek Çıktı 2
# Garip Değil

n = int(input("Bir tamsayı girin: "))

if n % 2 != 0:
    print("Garip")
elif n % 2 == 0 and n in range(2, 6):
    print("Garip Değil")
elif n % 2 == 0 and n in range(6, 21):
    print("Garip")
elif n % 2 == 0 and n > 20:
    print("Garip Değil")


# Bu program kullanıcıdan bir tamsayı alır ve verilen koşullara göre duruma uygun bir çıktı verir. Sizden bir tamsayı girmenizi isteyecektir. Ardından, girilen sayıya göre "Garip", "Garip Değil" veya hiçbir şey yazdıracaktır. 