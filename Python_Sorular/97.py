# Verilen bir sözlüğün değerlerini büyükten küçüğe sıralayan bir programı nasıl yazarsınız?



def sort_dictionary_values(dictionary):
    sorted_values = sorted(dictionary.values(), reverse=True)
    sorted_dict = {}
    for value in sorted_values:
        for key, val in dictionary.items():
            if val == value:
                sorted_dict[key] = value
                break
    return sorted_dict

# Örnek kullanım
my_dict = {'a': 5, 'b': 2, 'c': 8, 'd': 1}
sorted_dict = sort_dictionary_values(my_dict)
print(sorted_dict)



"""Bu programda sort_dictionary_values adında bir fonksiyon tanımlanır. Bu fonksiyon, bir sözlük alır ve sözlük değerlerini büyükten küçüğe sıralar.

Fonksiyonun içinde, sorted fonksiyonunu kullanarak sözlük değerlerini büyükten küçüğe sıralarız. reverse=True parametresi ile sıralamanın tersine çevrilmesini sağlarız.

Sıralanmış değerleri kullanarak yeni bir sözlük oluştururuz. İç içe döngüler kullanarak orijinal sözlüğü tararız. Her bir değeri, sıralanmış değerlerle karşılaştırarak eşleşen anahtarları yeni sözlüğe ekleriz.

Son olarak, sıralanmış sözlüğü döndürürüz.

Örnek kullanımda, my_dict adlı bir sözlük oluşturulur ve sort_dictionary_values fonksiyonu kullanılarak değerleri büyükten küçüğe sıralanmış bir sözlük elde edilir. Bu sıralanmış sözlük ekrana yazdırılır.
"""

"""EKRAN CIKTISI
{'c': 8, 'a': 5, 'b': 2, 'd': 1}
"""