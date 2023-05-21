# Örnek Soru 9.1 Dosya İsmini Sorgulayan Uygulama Sorusu: Girilen bir dosya isminin uzantısına bakarak (.py) o dosyanın bir Python programı olup olmadığını anlayan program yazınız.
def is_python_file(filename):
    if filename.endswith(".py"):
        return True
    else:
        return False

# Kullanıcıdan dosya adını al
filename = input("Dosya Adını Giriniz: ")
# Python programı kontrolü yap
if is_python_file(filename):
    print("Girilen dosya bir Python programıdır.")
else:
    print("Girilen dosya bir Python programı değildir.")

# Ekran Çıktıları
# Dosya Adını Giriniz: program.py
# Girilen dosya bir Python programıdır.

# Dosya Adını Giriniz: README.txt
# Girilen dosya bir Python programı değildir.


