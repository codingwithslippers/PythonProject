# Verilen bir liste içinde, ardışık olarak tekrar eden elemanları bulan bir programı nasıl yazarsınız?

def find_consecutive_duplicates(nums):
    duplicates = []
    
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            duplicates.append(nums[i])
    
    return duplicates

# Örnek kullanım
nums = [1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5]
consecutive_duplicates = find_consecutive_duplicates(nums)
print("Ardışık olarak tekrar eden elemanlar:", consecutive_duplicates)

"""

Bu programda, find_consecutive_duplicates fonksiyonu verilen liste üzerinde bir döngü kullanır. Her adımda, mevcut eleman ile bir sonraki eleman karşılaştırılır. Eğer iki eleman birbirine eşitse, bu eleman ardışık olarak tekrar eden bir elemandır ve duplicates listesine eklenir.

Sonuç olarak, consecutive_duplicates listesi ardışık olarak tekrar eden elemanları içerir.

Yukarıdaki örnekte, verilen liste [1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5] olduğunda, ardışık olarak tekrar eden elemanlar [2, 3, 5] olarak bulunur.

Bu yöntem, ardışık olarak tekrar eden elemanları bulmak için zaman karmaşıklığı O(n) olan etkili bir çözümdür, burada n liste uzunluğudur.

"""