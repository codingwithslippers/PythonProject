# Bir metin dosyasındaki en uzun satırı bulan bir programı nasıl yazarsınız?

def find_longest_line(filename):
    longest_line = ""
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if len(line) > len(longest_line):
                longest_line = line
    return longest_line

# Örnek kullanım
filename = 'metin_dosyasi.txt'
longest_line = find_longest_line(filename)
print("En uzun satır:", longest_line)



"""Bu programda, find_longest_line adında bir fonksiyon tanımlanır. Bu fonksiyon, belirtilen dosya adını alır, dosyayı satır satır okur ve en uzun satırı bulur.

Program, open fonksiyonunu kullanarak dosyayı okur ve with bloğu içinde açar. for döngüsü kullanılarak dosyanın her satırı üzerinde gezinilir. line.strip() ifadesi, satırın başındaki ve sonundaki boşlukları kaldırır. Ardından, len(line) ifadesi ile satırın uzunluğu hesaplanır ve longest_line ile karşılaştırılır. Eğer satırın uzunluğu longest_line'ın uzunluğundan daha büyükse, longest_line güncellenir.

Son olarak, longest_line fonksiyon tarafından döndürülür.

Örneğin, yukarıdaki kod çalıştırıldığında, 'metin_dosyasi.txt' adlı dosyadaki en uzun satır bulunur ve ekrana yazdırılır."""