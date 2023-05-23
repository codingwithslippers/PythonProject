from abc import ABC, abstractmethod

class SoyutSinif(ABC):
    def __init__(self, value):
        self.value = value
        super().__init__()

    @abstractmethod
    def islem(self):
        pass

class OnEkle(SoyutSinif):
    def islem(self):
        return self.value + 10

class OnCarp(SoyutSinif):
    def islem(self):
        return self.value * 10

# Ana program
x = OnEkle(5)
y = OnCarp(5)
print(x.islem())  # 15
print(y.islem())  # 50



