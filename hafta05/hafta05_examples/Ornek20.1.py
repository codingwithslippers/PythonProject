ST=0
sgn=+1
n=int (input('Terim Sayısı.:'))
for x in range (1, n+1):
    ST = ST+(1/x)*sgn
    sgn=-sgn
print ('Toplam=',ST)