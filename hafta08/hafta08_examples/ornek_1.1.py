# Liste veri yapılarına özgü metotları veren program çözümü:
for i in dir(list):
    if "__" not in i:
        print(i, end=',')
# Ekran Çıktısı
# append,clear,copy,count,extend,index,insert,pop,remove,reverse,sort,

# Demet (tuple) veri yapılarına özgü metotları veren program çözümü:
for i in dir(tuple):
    if "__" not in i:
        print(i, end=',')
# Ekran Çıktısı
# count,index,

# Küme (set) veri yapılarına özgü metotları veren program çözümü:
for i in dir(set):
    if "__" not in i:
        print(i, end=',')
# Ekran Çıktısı
# add,clear,copy,difference,difference_update,discard,intersection,intersection_update,isdisjoint,issubset,issuperset,pop,remove,symmetric_difference,symmetric_difference_update,union,update,

# Sözlük (dict) veri yapılarına özgü metotları veren program çözümü:
for i in dir(dict):
    if "__" not in i:
        print(i, end=',')
# Ekran Çıktısı
# clear,copy,fromkeys,get,items,keys,pop,popitem,setdefault,update,values,



