x= 33
for k in range (15, -1, -1):
    bit=x>>k & 1 
    print (bit,end=' ')
    if k % 4 == 0:
        print (end=' ')



