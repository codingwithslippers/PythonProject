# Dilimleme Yöntemi ile Çözüm
dil=("C", "C++", "C#", "Java", "Python", "ObjeC")
yeniDil=(dil[:5], "Swift")
print(yeniDil)

# Ekran Çıktısı
# (('C', 'C++', 'C#', 'Java', 'Python'), 'Swift')

# List Tipine Dönüşüm Yöntemi ile Çözüm
dil=("C", "C++", "C#", "Java", "Python", "ObjeC")
dil= list(dil)
dil.remove("ObjeC")
dil.append("Swift")
print(tuple(dil))

# Ekran Çıktısı
# ('C', 'C++', 'C#', 'Java', 'Python', 'Swift')



