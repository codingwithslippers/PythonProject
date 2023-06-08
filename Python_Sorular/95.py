# Bir CSV dosyasındaki verileri okuyup, belirli bir sütunda bulunan değerleri filtreleyen bir programı nasıl yazarsınız?


import csv

def filter_csv_data(filename, column_index, filter_value):
    filtered_data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[column_index] == filter_value:
                filtered_data.append(row)
    return filtered_data

# Örnek kullanım
filename = 'veriler.csv'
column_index = 2  # Filtrelemek istediğiniz sütunun indeksi
filter_value = 'A'  # Filtreleme yapmak istediğiniz değer
filtered_data = filter_csv_data(filename, column_index, filter_value)
for row in filtered_data:
    print(row)


"""Bu programda, filter_csv_data adında bir fonksiyon tanımlanır. Bu fonksiyon, belirtilen dosya adı, sütun indeksi ve filtre değerini alır. CSV dosyasını okur, belirtilen sütunda filtreleme yapar ve uygun verileri filtered_data listesine ekler.

Program, open fonksiyonunu kullanarak dosyayı okur ve with bloğu içinde açar. csv.reader fonksiyonu ile dosyadaki verileri okumak için bir okuyucu oluşturulur. Ardından, for döngüsü kullanılarak dosyanın her satırı üzerinde gezinilir. row[column_index] ifadesi ile belirtilen sütundaki değer alınır ve filter_value ile karşılaştırılır. Eğer değer, filtre değerine eşitse, o satır filtered_data listesine eklenir.

Son olarak, filtered_data listesi döndürülür ve döngü kullanarak filtrelenmiş veriler ekrana yazdırılır.

Örneğin, yukarıdaki kod çalıştırıldığında, 'veriler.csv' adlı CSV dosyası okunur, belirtilen sütunda 'A' değerine sahip olan satırlar filtrelenir ve ekrana yazdırılır. Sütun indeksi ve filtre değerini kendi gereksinimlerinize göre ayarlayabilirsiniz.
"""