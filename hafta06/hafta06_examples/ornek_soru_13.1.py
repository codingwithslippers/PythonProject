def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_list = fibonacci(n-1)
        fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list

sayi = 10
fibonacci_listesi = fibonacci(sayi)
print(f"Fibonacci serisi ({sayi} eleman): {fibonacci_listesi}")


'''

Bu örnekte, fibonacci() adlı özyinelemeli bir fonksiyon kullanılmıştır. Fonksiyon, n elemanlı Fibonacci serisini hesaplamak için kendisini tekrar çağırır.

Temel durumlarda (n <= 0, n == 1, n == 2), fonksiyon sırasıyla boş liste, [0] ve [0, 1] listesini döndürür. Bu temel durumlar, Fibonacci serisinin ilk iki elemanı olan 0 ve 1'i ifade eder.

Özyineleme durumunda ise fonksiyon, n-1 elemanlı Fibonacci serisini hesaplar ve son elemanına (fib_list[-1]) bir önceki elemanı (fib_list[-2]) ekleyerek n elemanlı Fibonacci serisini oluşturur.

Örnekte, sayi değişkenine 10 atanmıştır ve 10 elemanlı Fibonacci serisi hesaplanıp fibonacci_listesi adlı liste değişkenine atanır. Sonuç olarak, fibonacci_listesi ekrana yazdırılır.

Programın çıktısı şu şekilde olacaktır:

Fibonacci serisi (10 eleman): [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


'''