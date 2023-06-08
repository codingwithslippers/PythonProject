# Bir metin dosyasını okuyup, her bir satırın uzunluğunu hesaplayan bir programı nasıl yazarsınız?


def calculate_line_lengths(filename):
    with open(filename, 'r') as file:
        line_lengths = [len(line.strip()) for line in file]
    return line_lengths

# Örnek kullanım
filename = 'metin_dosyasi.txt'
line_lengths = calculate_line_lengths(filename)
print("Satır uzunlukları:", line_lengths)


"""Bu programda, calculate_line_lengths adında bir fonksiyon tanımlanır. Bu fonksiyon, belirtilen dosya adını alır, dosyayı okur ve her bir satırın uzunluğunu hesaplar.

Program, open fonksiyonunu kullanarak dosyayı okur ve with bloğu içinde açar. for döngüsü kullanılarak dosyanın her satırı üzerinde gezinilir. len(line.strip()) ifadesi, satırın başındaki ve sonundaki boşlukları kaldırarak satırın uzunluğunu hesaplar. Bu uzunluk, line_lengths listesine eklenir.

Son olarak, line_lengths listesi fonksiyon tarafından döndürülür.

Örneğin, yukarıdaki kod çalıştırıldığında, 'metin_dosyasi.txt' adlı dosyadaki her bir satırın uzunluğu hesaplanır ve ekrana yazdırılır."""