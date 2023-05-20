def ackermann(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    elif m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n - 1))

# Örnek kullanım
print(ackermann(3, 4))



'''

Bu örnekte, ackermann() adlı özyinelemeli bir fonksiyon tanımlanmıştır. Fonksiyon, m ve n parametrelerini alır ve Ancermann fonksiyonunun kurallarına göre değeri hesaplar.

Temel durumlar sırasıyla m == 0, m > 0 ve n == 0 olarak kontrol edilir. Temel durumlar yerine getirilmediğinde, fonksiyon kendisini tekrar çağırarak özyinelemeyi gerçekleştirir.

Örnekte, ackermann(3, 4) çağrısı yapılır ve sonuç olarak 125 elde edilir. Ancermann fonksiyonu, bu örnekte özyineleme işlemini üç kez gerçekleştirir ve sonucu hesaplar.

Ancermann fonksiyonu, büyük değerler için hızlı bir şekilde büyüme gösterdiği için yüksek m ve n değerleriyle çalıştığında performans sorunları ortaya çıkabilir. Bu nedenle, yüksek değerler için optimize edilmiş algoritmalar tercih edilmelidir.


Örnek olarak ackermann(3, 4) çağrısı yapıldığında, fonksiyon özyinelemeli olarak çalışacak ve sonuç olarak 125 döndürecektir.

ackermann(3, 4) çağrısının adım adım çıktısını anlatırsak:
1-İlk adımda, ackermann(3, 4) çağrısı yapılır.
2-Çünkü m > 0 ve n > 0, fonksiyon özyinelemeye girer ve ackermann(m - 1, ackermann(m, n - 1)) ifadesini hesaplamak için kendisini tekrar çağırır.
3-İkinci çağrıda, ackermann(3, 3) çağrısı yapılır.
4-Yine m > 0 ve n > 0 olduğu için fonksiyon özyinelemeye girer ve ackermann(m - 1, ackermann(m, n - 1)) ifadesini hesaplamak için kendisini tekrar çağırır.
5-Üçüncü çağrıda, ackermann(3, 2) çağrısı yapılır.
6-Hâlâ m > 0 ve n > 0 olduğu için fonksiyon özyinelemeye girer ve ackermann(m - 1, ackermann(m, n - 1)) ifadesini hesaplamak için kendisini tekrar çağırır.
7-Dördüncü çağrıda, ackermann(3, 1) çağrısı yapılır.
8-Bu sefer n == 0 olduğu için fonksiyon ackermann(m - 1, 1) ifadesini hesaplamak için kendisini tekrar çağırır.
9-Beşinci çağrıda, ackermann(2, 1) çağrısı yapılır.
10-Yine n == 0 olduğu için fonksiyon ackermann(m - 1, 1) ifadesini hesaplamak için kendisini tekrar çağırır.
11-Altıncı çağrıda, ackermann(1, 1) çağrısı yapılır.
12-Hâlâ n == 0 olduğu için fonksiyon ackermann(m - 1, 1) ifadesini hesaplamak için kendisini tekrar çağırır.
13-Yedinci çağrıda, ackermann(0, 1) çağrısı yapılır.
14-Bu sefer m == 0 olduğu için fonksiyon n + 1 ifadesini hesaplar ve sonuç olarak 2 döndürür.
15-Altıncı çağrı, beşinci çağrı, dördüncü çağrı, üçüncü çağrı ve ikinci çağrı sırasıyla 2 değerini alır ve ackermann(1, 2) çağrısını hesaplar
16-Bu işlem sırasıyla geriye doğru devam eder ve sonunda ilk çağrı olan ackermann(3, 4) sonucu olarak 125 döndürülür.
17-Programın çıktısı olarak 125

'''