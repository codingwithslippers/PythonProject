# 1. Bir programlama dili ile kod yazımında karşılaşılan olası hatalar şunlardır:
#    - Sözdizimi Hataları: Kodun dilbilgisi kurallarına uymaması durumunda ortaya çıkar.
#    - Yürütme Hataları (Runtime Errors): Kodun çalışma zamanında hatalı bir durumla karşılaşması durumunda ortaya çıkar.
#    - Mantıksal Hatalar: Kodun istenen işlevi doğru şekilde yerine getirmemesi durumunda ortaya çıkar.

# 2. Python dilinde tüm yerleşik istisna tipleri BaseException sınıfının alt sınıflarıdır. Bazı yaygın kullanılan yerleşik istisna tipleri şunlardır:
#    - Exception: Tüm istisna tiplerinin temel sınıfıdır.
#    - TypeError: Yanlış veri türü kullanımı durumunda ortaya çıkar.
#    - ValueError: Yanlış değer kullanımı durumunda ortaya çıkar.
#    - ZeroDivisionError: Sıfıra bölme hatası durumunda ortaya çıkar.

# 3. `try` kelimesi tek başına kullanılamaz, her zaman en az bir `except` bloğuyla birlikte kullanılmalıdır. Ayrıca, `finally` bloğu da kullanılabilir. Örnek kullanım:
#    try:
#        # Kodun hata üretebilecek bölümü
#    except ExceptionType:
#        # Belirli bir hata türü için işlemler
#    finally:
#        # Her durumda çalışacak işlemler

# 4. "IndexError: list index out of range" hatası, bir liste üzerinde geçersiz bir indeksleme yapmaya çalıştığımızda ortaya çıkar. Bu hata genellikle aşağıdaki durumlarla ilişkilidir:
#    - Bir listenin veya dizinin boyutundan daha büyük veya negatif bir indeks değeri kullanmak.
#    - Bir boş liste veya diziye erişim yapmaya çalışmak.

# 5. Eğer normalde programın hata oluşturma ihtimali yoksa, ancak belirli bir durumda kullanıcıya uyarı mesajı göndermek istiyorsanız, `assert` ifadesini kullanabilirsiniz. Örnek kullanım:
#    assert expression, "Uyarı mesajı"
#    `expression` ifadesi doğru (True) olmalıdır. Eğer ifade yanlış (False) ise, belirtilen uyarı mesajıyla birlikte AssertionError istisnası oluşur.

# 6. Olası tüm hataları veren bir Python kodu aşağıdaki gibi olabilir:

try:
    # Potansiyel hata üretebilecek kod bloğu
    a = 10
    b = 0
    c = a / b
    d = int("abc")
    e = [1, 2, 3]
    print(e[4])
except Exception as e:
    # Tüm istisna tipleri için ortak işlemler
    print("Bir hata oluştu:", str(e))

