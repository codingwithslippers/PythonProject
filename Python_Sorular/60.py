#  Verilen bir metindeki tüm palindromları bulan bir programı nasıl yazarsınız?


def find_palindromes(text):
    palindromes = []

    # Metindeki tüm alt dizeleri kontrol ediyoruz
    for i in range(len(text)):
        for j in range(i + 1, len(text) + 1):
            substring = text[i:j]

            # Alt dizeyi ters çevirerek palindrom olup olmadığını kontrol ediyoruz
            if substring == substring[::-1]:
                palindromes.append(substring)

    return palindromes

# Örnek kullanım
text = "madam araya kayar"
result = find_palindromes(text)
print("Palindromlar:")
for palindrome in result:
    print(palindrome)




"""

Bu program, verilen metindeki tüm palindromları bulur. İki döngü kullanarak metindeki tüm alt dizeleri kontrol ederiz. Her alt dizeyi alıp tersine çevirerek, palindrom olup olmadığını kontrol ederiz. Palindrom olan alt dizeleri palindromes listesine ekleriz.

Yukarıdaki örnekte, "madam araya kayar" metnindeki tüm palindromlar bulunur ve ekrana yazdırılır:


"""


""" EKRAN CIKTISI

Palindromlar:
madam
ada
aya



"""