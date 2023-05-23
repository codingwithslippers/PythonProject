class Fibonacci:
    def __init__(self, limit):
        self.limit = limit
        self.prev = 0
        self.curr = 1
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= self.limit:
            raise StopIteration
        else:
            result = self.prev
            self.prev, self.curr = self.curr, self.prev + self.curr
            self.counter += 1
            return result

# Fibonacci serisinin ilk 10 sayısını hesaplayalım ve çıktıyı verelim
f = Fibonacci(10)
for num in f:
    print(num)

# EKRAN ÇIKTISI
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34