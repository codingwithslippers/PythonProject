from collections import deque

kyrk= deque(["Erlik","Ahmet","Solmaz"])
kyrk.append("Mehmet")
kyrk.append("Gizem")
kyrk.popleft()
kyrk.popleft()
print(list(kyrk))

# Ekran Çıktısı
# ['Solmaz', 'Mehmet', 'Gizem']


