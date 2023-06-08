# Bir string içerisinde belirlenen bir karakterin olup olmadığını kontrol eden Python programıni yaziniz. (Kontrol etme işlemi fonksiyon içinde yapılmıştır.)

def kontrol(str):
  sayac = 0
  for ch in str:
    if ch == 'ğ':
      sayac = sayac + 1
 
  if sayac == 1:
    return True
  else:
    return False
 
metin=input('Metin : ')
if(kontrol(metin)==True):
      print('ğ karakteri metin içinde var')
else:
      print('ğ karakteri metin içinde yok')