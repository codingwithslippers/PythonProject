# Verilen bir listedeki tüm alt kümelerin toplamını bulan bir programı nasıl yazarsınız?

def find_subset_sums(nums):
    subsets = []
    subset_sums = []
    
    def backtrack(start, subset):
        subsets.append(subset[:])
        subset_sum = sum(subset)
        subset_sums.append(subset_sum)
        
        for i in range(start, len(nums)):
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
    
    backtrack(0, [])
    
    return subset_sums

# Örnek kullanım
nums = [1, 2, 3]
subset_sums = find_subset_sums(nums)
print("Alt kümelerin toplamları:", subset_sums)



"""
Bu programda, find_subset_sums fonksiyonu verilen liste üzerinde özyinelemeli bir backtrack fonksiyonunu çağırır. backtrack fonksiyonu, başlangıç indeksi ve mevcut alt küme parametrelerini alır.

Her adımda, subsets listesine mevcut alt küme eklenir ve alt kümenin toplamı hesaplanarak subset_sums listesine eklenir.

Daha sonra, başlangıç indeksinden itibaren listenin geri kalan elemanları üzerinde bir döngü kullanarak özyinelemeli olarak tüm alt kümeleri buluruz. Her adımda, mevcut eleman alt kümeye eklenir, backtrack fonksiyonu recursive olarak çağırılır ve sonrasında mevcut eleman alt kümeden çıkarılır.

Sonuç olarak, subset_sums listesi tüm alt kümelerin toplamlarını içerir.

Yukarıdaki örnekte, verilen liste [1, 2, 3] olduğunda, alt kümelerin toplamları [0, 1, 2, 3, 3, 4, 5, 6] olarak bulunur. İlk eleman olan 0, boş kümenin toplamını temsil eder.

Bu yöntem, tüm alt kümelerin toplamlarını bulmak için zaman karmaşıklığı O(2^n) olan bir yöntemdir, burada n liste uzunluğudur.
"""