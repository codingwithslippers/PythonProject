# Bir metin dosyasındaki tüm satırları ters çeviren bir programı nasıl yazarsınız?


def reverse_lines(filename):
    reversed_lines = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            reversed_line = line[::-1]  # Satırı ters çevir
            reversed_lines.append(reversed_line)
    return reversed_lines

# Örnek kullanım
filename = 'metin.txt'
reversed_lines = reverse_lines(filename)
for line in reversed_lines:
    print(line)




"""Bu programda, reverse_lines adında bir fonksiyon tanımlanır. Bu fonksiyon, belirtilen dosya adını alır ve dosyadaki satırları ters çevirir.

Program, open fonksiyonunu kullanarak dosyayı okur ve with bloğu içinde açar. Dosyanın tüm satırları readlines fonksiyonuyla okunur ve lines listesine atılır. Ardından, for döngüsü kullanılarak her satır üzerinde gezinilir. Satır, ters çevirmek için line[::-1] ifadesiyle ters çevrilir ve reversed_lines listesine eklenir.

Son olarak, reversed_lines listesi döndürülür ve döngü kullanarak ters çevrilmiş satırlar ekrana yazdırılır.

Örneğin, yukarıdaki kod çalıştırıldığında, 'metin.txt' adlı metin dosyası okunur, satırlar ters çevrilir ve ekrana yazdırılır.
"""