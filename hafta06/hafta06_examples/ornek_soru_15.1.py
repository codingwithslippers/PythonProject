def hanoi(n, baslangic, yardimci, hedef):
    if n > 0:
        # Adım 1: (n-1) diskini yardımcı çubuğa taşı
        hanoi(n - 1, baslangic, hedef, yardimci)
        
        # Adım 2: En büyük diskini hedef çubuğa taşı
        print(f"{baslangic} çubuğundaki {n}. diskini {hedef} çubuğuna taşı")
        
        # Adım 3: (n-1) diskini hedef çubuğuna taşı
        hanoi(n - 1, yardimci, baslangic, hedef)

# Örnek kullanım
n = 3
hanoi(n, "A", "B", "C")

'''

Hanoi Kuleleri problemi çözümünü adım adım anlatalım:
1- Başlangıç durumu: İlk çubukta, en küçük disk en üstte olacak şekilde farklı büyüklükte n adet disk bulunuyor. Diğer iki çubuk boş.
2- Adım 1: (n-1) diskini yardımcı çubuğa taşıma:
    * İlk adımda, en büyük disk hariç (n-1) adet diskimizi yardımcı çubuğa taşımamız gerekiyor.
    * Bu adımı gerçekleştirmek için özyinelemeli olarak hanoi(n - 1, baslangic, hedef, yardimci) çağrısı yapılır.
    * Bu çağrı, en büyük olmayan diskleri baslangic çubuğundan yardimci çubuğuna taşır.
3- Adım 2: En büyük diski hedef çubuğa taşıma:
    * En büyük disk, başlangıç çubuğunda en altta bulunur.
    * Bu disk, başlangıç çubuğundan hedef çubuğuna doğrudan taşınır.
    * Bu adımı gerçekleştirmek için print(f"{baslangic} çubuğundaki {n}. diskini {hedef} çubuğuna taşı") ifadesi kullanılır.
4- Adım 3: (n-1) diskini hedef çubuğuna taşıma:
    * Adım 1'de yardımcı çubuğa taşınan diskleri, hedef çubuğuna taşımamız gerekiyor.
    * Bu adımı gerçekleştirmek için özyinelemeli olarak hanoi(n - 1, yardimci, baslangic, hedef) çağrısı yapılır.
    * Bu çağrı, yardımcı çubuktaki diskleri yardimci çubuğundan hedef çubuğuna taşır.

Bu adımlar, özyinelemeli bir şekilde tekrarlanır ve sonunda tüm diskler hedef çubuğuna doğru taşınır. Programın çıktısı olarak, disklerin çubuklar arasında nasıl taşındığını adım adım görebilirsiniz.

Örnek bir senaryo için, n = 3 olarak varsayalım:
    1- Başlangıç durumu:
        * A çubuğu: 3 2 1 (en küçük disk en üstte)
        * B çubuğu: boş
        * C çubuğu: boş
    2- Adım 1: (n-1) diskini yardımcı çubuğa taşıma:
        * A çubuğundaki 2 ve 1 numaralı diskleri B çubuğuna taşıyoruz.
        * Adımlar:
            * disk: A -> C
            * disk: A -> B
'''