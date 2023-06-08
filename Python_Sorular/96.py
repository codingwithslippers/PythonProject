#  Bir JSON dosyasını okuyup, içindeki verileri analiz eden bir programı nasıl yazarsınız?


import json

def analyze_json_data(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        # JSON verilerini analiz etmek için uygun işlemleri gerçekleştirin
        # Örnek olarak, JSON verilerini ekrana yazdırabilirsiniz
        print(data)

# Örnek kullanım
filename = 'veriler.json'
analyze_json_data(filename)


"""Bu programda, analyze_json_data adında bir fonksiyon tanımlanır. Bu fonksiyon, belirtilen dosya adını alır, dosyayı açar ve JSON verilerini analiz etmek için uygun işlemleri gerçekleştirir.

Program, open fonksiyonunu kullanarak dosyayı okur ve with bloğu içinde açar. json.load fonksiyonu kullanılarak dosyadaki JSON verileri yüklenir ve data değişkenine atanır. Bu aşamada, data değişkeni Python sözlükleri ve listeleri gibi uygun veri yapılarını içerir.

JSON verilerini analiz etmek için yapılacak işlemler programın gereksinimlerine bağlıdır. Örneğin, JSON verilerini ekrana yazdırmak için print(data) ifadesi kullanılabilir. Diğer işlemleri bu noktada gerçekleştirebilirsiniz.

Örneğin, yukarıdaki kod çalıştırıldığında, 'veriler.json' adlı JSON dosyası okunur ve JSON verileri ekrana yazdırılır. Bu noktada, data değişkenini kullanarak JSON verilerini analiz edebilirsiniz."""