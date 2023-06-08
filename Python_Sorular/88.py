# Bir metin dosyasındaki karakter sayısını bulan bir programı nasıl yazarsınız?


def count_characters(filename):
    with open(filename, 'r') as file:
        text = file.read()
        character_count = len(text)
    return character_count

# Örnek kullanım
filename = 'metin_dosyasi.txt'
characters = count_characters(filename)
print("Karakter sayısı:", characters)


"""Bu programda, count_characters adında bir fonksiyon tanımlanır. Bu fonksiyon, belirtilen dosya adını alır, dosyayı okur ve dosyadaki karakter sayısını hesaplar.

Program, open fonksiyonunu kullanarak dosyayı okur ve with bloğu içinde açar. Dosyanın içeriği file.read() ile okunur ve text değişkenine atanır. Ardından, len(text) ifadesi kullanılarak text içindeki karakter sayısı hesaplanır ve character_count değişkenine atanır. Fonksiyon tarafından döndürülür.

Örneğin, yukarıdaki kod çalıştırıldığında, 'metin_dosyasi.txt' adlı dosyadaki karakter sayısı hesaplanır ve ekrana yazdırılır."""