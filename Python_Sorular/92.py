# Bir metin dosyasını kopyalayan bir programı nasıl yazarsınız?


def copy_file(source_file, destination_file):
    with open(source_file, 'r') as source:
        with open(destination_file, 'w') as destination:
            for line in source:
                destination.write(line)

# Örnek kullanım
source_file = 'kaynak.txt'
destination_file = 'hedef.txt'
copy_file(source_file, destination_file)



"""
Bu programda, copy_file adında bir fonksiyon tanımlanır. Bu fonksiyon, kaynak dosya adı ve hedef dosya adı olmak üzere iki parametre alır.

Program, open fonksiyonunu 'r' (read) moduyla kaynak dosya için ve 'w' (write) moduyla hedef dosya için kullanarak dosyaları açar. Kaynak dosya source ve hedef dosya destination adıyla referanslanır.

Daha sonra, kaynak dosyadaki her satır for döngüsüyle okunur ve hedef dosyaya yazılır. write fonksiyonu kullanılarak kaynak dosyadan okunan her satır hedef dosyaya yazılır.

Örneğin, yukarıdaki kod çalıştırıldığında, 'kaynak.txt' adlı dosyanın içeriği 'hedef.txt' adlı dosyaya kopyalanır.
"""