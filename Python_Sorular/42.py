# Kullanıcının girdiği üç kenar bilgisine göre üçgenin tipini belirleyen eğer girilen kenarları uzunlukları bir üçgen oluşturmuyorsa bunu bildiren kodu yazınız. ( mutlak değer içinde iki kenarın farkı alınır eğer fark diğer kenardan büyükse girilen değerler üçgen oluşturmaz. Bu işlem tüm kenarlar için yapılır.

tip = input("Tipini bulmak istediğiniz şekil? (1-Üçgen, 2-Dörtgen): ")

if tip == "1":
    a = int(input("1. kenar: "))
    b = int(input("2. kenar: "))
    c = int(input("3. kenar: "))
    
    if abs(b-c) < a and a < b+c and abs(c-a) < b and b < a+c and abs(a-b) < c and c < a+b:
        if (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
            print("İkizkenar Üçgen!")
        elif a == b == c:
            print("Eşkenar Üçgen!")
        else:
            print("Normal Üçgen!")
    else:
        print("Girdiğiniz Değerler Üçgen Oluşturmuyor.")

elif tip == "2":
    a = int(input("1. kenar: "))
    b = int(input("2. kenar: "))
    c = int(input("3. kenar: "))
    d = int(input("4. kenar: "))

    if a == b == c == d:
        print("Kare!")
    elif a == c and b == d:
        print("Dikdörtgen!")
    else:
        print("Normal Dörtgen!")
    
else:
    print("Geçersiz tip seçimi!")
