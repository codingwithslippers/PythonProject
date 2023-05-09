while True :
    s1 = int(input("s1....:"))
    s2 = int(input("s2....:"))
    op = input("işlem...:")
    if (op== "+"):
        S = s1 + s2
    elif (op == "-"):
        S = s1 - s2
    elif (op == "*"):
        S = s1 * s2
    elif (op == "/"):
        S = s1 / s2
    else:
        print ("Hatalı seçim gerçekleçtirdiniz...")
    print ("Sonuç=", S)
    cvp = input("Devam etmek istiyor musunuz (e/h) ?")
    if cvp =="h":
        break
    else:
        continue
print ("Hesap makinesi kapandı.")