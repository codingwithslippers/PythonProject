# Aşağıdaki görselin ekran çıktısını veren python kodlarını döngü kullanarak yazınız?
"""
*****
****
***
**
*
"""


satir=6
for i in range(satir):
   print(''*(3*i+1) + '*'*(satir - i - 1))
