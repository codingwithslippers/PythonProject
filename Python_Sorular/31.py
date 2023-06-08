#  Kullanıcının girdiği 4 basamaklı sayıyı basamaklarını ayırıp tek tek rakamlarını ve rakamlarının toplamını ekrana yazdıran python kodlarını yazınız?

# Örnek: kullanıcı 3491 rakamı girmiş ise ekran çıktısı aşağıdaki gibi olacaktır.
# 3
# 4
# 9 
# 1
# toplam: 17


sayi=input("sayi gir: ")
lst=list(sayi)
#her rakama ayrı ayrı şekilde alt alta yazdırıyoruz
for y in lst:
   print(y)
i = 0
x = int(sayi)
if len(str(x)) == 4:
   #sayıyı basamaklarına ayırıp, ayrı ayrı değişkenlere atama yaparak her bir değişkeni topluyoruz
   bir = x % 10
   x = str(x)
   x = x[:-1]
   x = int(x)
   on = x % 10
   x = str(x)
   x = x[:-1]
   x = int(x)
   yuz = x % 10
   x = str(x)
   x = x[:-1]
   x = int(x)
   bin = x % 10
   print("toplam:",bir+on + yuz + bin)
else:
   print("Girdiginiz deger 4 basamakli degil")


