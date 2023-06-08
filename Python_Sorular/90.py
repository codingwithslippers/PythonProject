# Bir metin dosyasında belirli bir kelimenin kaç kez geçtiğini bulan bir programı nasıl yazarsınız?

def count_word_occurrences(filename, target_word):
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            count += words.count(target_word)
    return count

# Örnek kullanım
filename = 'metin_dosyasi.txt'
target_word = 'kelime'
occurrences = count_word_occurrences(filename, target_word)
print(f"'{target_word}' kelimesi dosyada {occurrences} kez geçiyor.")



"""Bu programda, count_word_occurrences adında bir fonksiyon tanımlanır. Bu fonksiyon, belirtilen dosya adını ve hedef kelimeyi alır, dosyayı satır satır okur ve hedef kelimenin kaç kez geçtiğini hesaplar.

Program, open fonksiyonunu kullanarak dosyayı okur ve with bloğu içinde açar. for döngüsü kullanılarak dosyanın her satırı üzerinde gezinilir. Her satır, split() yöntemiyle kelimelere ayrılır ve words listesine atanır. count(target_word) ifadesi, words listesinde hedef kelimenin kaç kez geçtiğini hesaplar ve bu sayı count değişkenine eklenir.

Son olarak, count değişkeni fonksiyon tarafından döndürülür.

Örneğin, yukarıdaki kod çalıştırıldığında, 'metin_dosyasi.txt' adlı dosyada 'kelime' kelimesinin kaç kez geçtiği hesaplanır ve ekrana yazdırılır."""