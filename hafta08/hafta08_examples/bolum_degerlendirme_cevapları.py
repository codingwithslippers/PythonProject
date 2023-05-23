#1 Son giren - İlk çıkar (Last In - First Out (LIFO)) mantığı ile çalışan ve ara elemanlara erişimin doğrudan yapılamadığı özel yapıya "Yığın (Stack)" adı verilir.

#2 İlk giren - İlk çıkar (First-In-First-Out (FIFO)) mantığı ile çalışan ve ara elemanlara erişimin doğrudan yapılamadığı özel yapıya "Kuyruk (Queue)" adı verilir.

#3 Veri tipini bilmediğimiz bir nesnenin hangi veri yapısına ait olduğunu öğrenmek için type() fonksiyonunu kullanabiliriz. Örneğin, type(nesne) şeklinde kullanarak nesnenin veri tipini öğrenebiliriz. Çıktı olarak veri yapısının adını verecektir.

#4 Python'da boş bir küme tanımlamak için {} veya set() kullanabiliriz. Örneğin, bos_kume = {} veya bos_kume = set() şeklinde tanımlayabiliriz.

#5 Liste ve demet veri yapıları arasındaki temel fark, listenin değiştirilebilir (mutable) olduğu ancak demetin değiştirilemez (immutable) olduğudur. Yani, bir listeye eleman ekleme, çıkarma veya değiştirme yapabilirken, bir demetin elemanlarını değiştirmek mümkün değildir.

#6 Aşağıdaki programın çıktısı ne olur?
i=[]
kg = {'elma': 32, 'muz': 47, 'nar': 17}
print (type (kg))
print (type (i))

# EKRAN ÇIKTILARI
# <class 'dict'>
# <class 'list'>

#7 Aşağıdaki program istenen satır-sütun değerinde matris oluşturmaktadır. Buna göre 4*3'lük bir matrisi ekrana yazdırmak için ana programda eksik bırakılan alana ne yazılmalıdır?
def matris(row, col):
    matrix = []
    for _ in range(row):
        matrix.append([0] * col)
    return matrix

row = int(input("Satır sayısını girin: "))
col = int(input("Sütun sayısını girin: "))

print(matris(row, col))


#   EKRAN ÇIKTILARI
# [ [0, 0, 0, 0],
#   [0, 0, 0, 0],
#   [0, 0, 0, 0]]


#8 Aşağıdaki program parçasının çalışmasından sonra A listesinin ilk ve son elemanları hangi değerleri alır?
A = (-1, 1, -1, 1, -1)
for i in range(5):
    A = A + (i+1,)
print(A)

# EKRAN ÇIKTISI
# (-1, 1, -1, 1, -1, 1, 2, 3, 4, 5)



#9 Aşağıdaki küme tanımlamalarından hangileri geçerlidir?
k={1, 2, 3, 4}
k={{1, 2}, {3, 4}}
k={[1, 2], [3, 4] }


# EKRAN ÇIKTISI
# Küme tanımlamalarında her bir eleman eşsiz olmalıdır ve değiştirilemez (immutable) veri tipleri kullanılmalıdır. Buna göre geçerli ve geçersiz küme tanımlamalarını inceleyelim:

# Geçerli küme tanımlamaları:

# k = {1, 2, 3, 4}: Bu tanımlama geçerlidir. Küme içerisinde sayısal değerler kullanılmıştır ve her bir değer eşsizdir.
# Geçersiz küme tanımlamaları:

# k = {{1, 2}, {3, 4}}: Bu tanımlama geçersizdir. İç içe küme tanımlaması yapılmıştır, ancak küme elemanları değiştirilemez olmalıdır ve içerisinde başka bir küme bulunamaz.
# k = {[1, 2], [3, 4]}: Bu tanımlama geçersizdir. Değiştirilebilir (mutable) bir veri tipi olan liste kullanılmıştır, ancak küme elemanları değiştirilemez olmalıdır.
# Sonuç olarak, sadece "k = {1, 2, 3, 4}" tanımlaması geçerli bir küme tanımlamasıdır.





