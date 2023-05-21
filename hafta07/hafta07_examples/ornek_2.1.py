# Örnek: Bir stringi silen program yazınız.
s='Ahmet'
print(s)
del s
print(s)


# EKRAN ÇIKTISI
'''
Ahmet
Traceback (most recent call last):
  File "c:\Users\salih\OneDrive\Masaüstü\PythonBitirmeProjesi\DOSYA\hafta07\hafta07_examples\ornek_2.1.py", line 5, in <module>
    print(s)
          ^
NameError: name 's' is not defined
'''


s.isalnum()
s.isalpha()
s.isdecimal()
s.isdigit()
s.isidentifier()
s.islower()
s.isnumeric()
s.isprintable()
s.ispace()
s.istitle()
s.isupper()
