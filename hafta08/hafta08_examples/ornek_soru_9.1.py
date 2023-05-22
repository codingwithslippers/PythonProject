# Bir öğrencinin adını, soyadını ve notlarını içeren bir tuple oluşturun. Daha sonra bu tuple'ı kullanarak öğrencinin adını, soyadını ve not ortalamasını ekrana yazdırın.
student = ("John", "Doe", (85, 90, 95, 88, 92))

name = student[0]
surname = student[1]
grades = student[2]
average = sum(grades) / len(grades)

print("Öğrenci Adı:", name)
print("Öğrenci Soyadı:", surname)
print("Not Ortalaması:", average)


