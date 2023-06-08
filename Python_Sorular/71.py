# Verilen iki sıralı listenin kesişimini bulan bir programı nasıl yazarsınız?


def find_intersection(list1, list2):
    intersection = []
    i = 0
    j = 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            intersection.append(list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    
    return intersection

# Örnek kullanım
list1 = [1, 3, 5, 7, 9]
list2 = [2, 3, 6, 7, 8, 9]
intersection = find_intersection(list1, list2)
print("Kesişim:", intersection)


"""
Bu programda, find_intersection fonksiyonu iki sıralı listeyi parametre olarak alır. Ardından, iki liste üzerinde iki işaretçi (i ve j) kullanarak ilerler. Her adımda, iki işaretçinin gösterdikleri elemanları karşılaştırır. Eğer elemanlar eşitse, bu elemanı kesişim listesine ekler ve her iki işaretçiyi de bir ileri taşır. Eğer list1[i] küçükse, list1'in bir sonraki elemanını kontrol etmek için i'yi bir ileri taşır. Eğer list2[j] küçükse, list2'nin bir sonraki elemanını kontrol etmek için j'yi bir ileri taşır.

Program sonucunda, intersection listesi iki listenin kesişimini içerecektir. Yukarıdaki örnekte, list1 ve list2'nin kesişimi [3, 7, 9] olarak bulunacaktır.

Bu yöntem, iki sıralı liste üzerinde tek bir döngüyle geçtiği için zaman karmaşıklığı O(min(n, m)) olacaktır, burada n ve m listenin boyutlarıdır.
"""