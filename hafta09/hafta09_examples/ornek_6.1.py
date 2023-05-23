class Hayvan:
    def Konus(self):
        pass

class Inek(Hayvan):
    def Konus(self):
        print("Mooo")

class Kedi(Hayvan):
    def Konus(self):
        print("Miyav")

class Kopek(Hayvan):
    def Konus(self):
        print("Hav Hav")

# Ana program
hayvanlar = [Inek(), Kedi(), Kopek()]

for hayvan in hayvanlar:
    hayvan.Konus()


# EKRAN ÇIKTISI
# Mooo
# Miyav
# Hav Hav


