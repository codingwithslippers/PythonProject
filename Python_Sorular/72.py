# Verilen bir liste içinde, toplamı en büyük olan ardışık alt listeyi, herhangi bir elemanı çıkarmadan bulan bir programı nasıl yazarsınız?

def find_max_subarray(nums):
    max_sum = float('-inf')  # Başlangıçta en küçük değer olarak varsayılan negatif sonsuzluk
    current_sum = 0
    start_index = 0
    end_index = 0
    current_start_index = 0
    
    for i in range(len(nums)):
        current_sum += nums[i]
        
        if current_sum > max_sum:
            max_sum = current_sum
            start_index = current_start_index
            end_index = i
        
        if current_sum < 0:
            current_sum = 0
            current_start_index = i + 1
    
    return nums[start_index:end_index+1]

# Örnek kullanım
nums = [1, -3, 5, -2, 9, -8, -6, 4]
max_subarray = find_max_subarray(nums)
print("En büyük ardışık alt liste:", max_subarray)

"""

Bu programda, find_max_subarray fonksiyonu verilen liste üzerinde bir döngü kullanır. Her adımda, current_sum değişkenine mevcut eleman eklenir. Eğer current_sum, mevcut en büyük toplam (max_sum) değerini aşarsa, max_sum, start_index ve end_index güncellenir.

Eğer current_sum negatif bir değere düşerse, alt listeyi sıfırlamak için current_sum sıfırlanır ve current_start_index bir sonraki elemandan başlar.

Sonuç olarak, nums[start_index:end_index+1] ifadesiyle en büyük ardışık alt liste elde edilir.

Yukarıdaki örnekte, verilen liste [1, -3, 5, -2, 9, -8, -6, 4] olduğunda, en büyük ardışık alt liste [5, -2, 9] olarak bulunur.

Bu yöntem, zaman karmaşıklığı O(n) olan etkili bir çözümdür, burada n liste uzunluğudur.

"""

