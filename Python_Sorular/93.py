# Bir metin dosyasına yeni bir satır ekleyen bir programı nasıl yazarsınız?


def add_line_to_file(filename, line):
    with open(filename, 'a') as file:
        file.write(line + '\n')

# Örnek kullanım
filename = 'metin.txt'
new_line = 'Bu yeni bir satır.'
add_line_to_file(filename, new_line)


"""Bu programda, add_line_to_file adında bir fonksiyon tanımlanır. Bu fonksiyon, belirtilen dosya adını ve eklenecek satırı alır.

Program, open fonksiyonunu 'a' (append) moduyla kullanarak dosyayı açar. Bu mod, dosyanın sonuna ekleme yapılmasını sağlar. Dosya with bloğu içinde açılır ve file adıyla referanslanır.

Sonrasında, write fonksiyonu kullanılarak line değişkenindeki satır dosyaya yazılır. Satırın sonuna '\n' karakteri eklenerek yeni bir satır oluşturulur.

Örneğin, yukarıdaki kod çalıştırıldığında, 'metin.txt' adlı dosyanın sonuna 'Bu yeni bir satır.' şeklinde bir satır eklenir."""
