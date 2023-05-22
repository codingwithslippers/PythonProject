def check_parentheses(text):
    stack = []  # Parantezleri tutmak için bir stack oluşturuyoruz

    # Metindeki her karakteri kontrol ediyoruz
    for char in text:
        if char == "(":
            stack.append(char)  # Açma parantezi ise stack'e ekliyoruz
        elif char == ")":
            if len(stack) == 0 or stack[-1] != "(":
                return False  # Eşleşmeyen kapanma parantezi bulundu
            stack.pop()  # Eşleşen açma parantezini stack'ten çıkarıyoruz

    return len(stack) == 0  # Tüm parantezler eşleştiyse stack boş olmalı

# Test etmek için örnek metinleri kullanalım
text1 = "((()))"
text2 = "()()()"
text3 = "(()))"
text4 = "())("

print(check_parentheses(text1))  # True
print(check_parentheses(text2))  # True
print(check_parentheses(text3))  # False
print(check_parentheses(text4))  # False



