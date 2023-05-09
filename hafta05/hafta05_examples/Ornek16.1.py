N=5
for a in range (N):
    for b in range (2*N+1):
        if b < N -a or b > N + a:
            print('1',end=' ')
        else:
            print('0',end=' ')
    # b döngüsü sonu
    print('\n')
#a döngüsü sonu


