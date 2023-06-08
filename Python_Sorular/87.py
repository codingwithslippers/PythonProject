# Bir metin dosyasındaki satır sayısını bulan bir programı nasıl yazarsınız?


def count_lines(filename):
    with open(filename, 'r') as file:
        line_count = sum(1 for line in file)
    return line_count

# Örnek kullanım
filename = 'metin_dosyasi.txt'
lines = count_lines(filename)
print("Satır sayısı:", lines)


"""Bu programda, count_lines adında bir fonksiyon tanımlanır. Bu fonksiyon, belirtilen dosya adını alır ve dosyanın satır sayısını hesaplar.

Program, open fonksiyonunu kullanarak dosyayı okur ve with bloğu içinde açar. sum(1 for line in file) ifadesi, dosyanın her satırı için 1 ekleyerek toplam satır sayısını hesaplar. Sonuç, line_count değişkenine atanır ve fonksiyon tarafından döndürülür.

Örneğin, yukarıdaki kod çalıştırıldığında, 'metin_dosyasi.txt' adlı dosyadaki satır sayısı hesaplanır ve ekrana yazdırılır."""