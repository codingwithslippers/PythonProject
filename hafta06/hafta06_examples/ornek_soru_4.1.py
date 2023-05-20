cevir = lambda fahrenheit: (fahrenheit - 32) * 5/9

# Kullanıcıdan Fahrenheit sıcaklığını al
fahrenheit = float(input("Fahrenheit sıcaklığını girin: "))

# Dereceye çevir
derece = cevir(fahrenheit)

# Sonucu ekrana yazdır
print("Derece:", derece)


'''
cevir adlı lambda fonksiyonu tanımlanır. Bu fonksiyon, fahrenheit adında bir parametre alır ve (fahrenheit - 32) * 5/9 ifadesini kullanarak Fahrenheit sıcaklığını Derece'ye çevirir.

Ana programda kullanıcıdan Fahrenheit sıcaklığını alır.

cevir lambda fonksiyonunu çağırarak Fahrenheit sıcaklığını Derece'ye çevirir ve sonucu derece değişkenine atar.

Sonucu ekrana yazdırmak için print() fonksiyonunu kullanır.

'''