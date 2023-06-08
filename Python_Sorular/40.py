 # Çarpım tablosunu ekrana yazan python kodunu yazınız.

for i in range(1,10):
    print("*************************")
    for k in range(1,10):
        print("{} x {} = {}".format(k,i,i*k))