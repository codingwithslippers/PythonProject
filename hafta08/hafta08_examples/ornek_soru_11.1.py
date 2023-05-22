# Küme işlemleri için örnek kümeler
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Birleşim kümesi
birlesim = A.union(B)
print("Birleşim Kümesi:", birlesim)

# Kesişim kümesi
kesisim = A.intersection(B)
print("Kesişim Kümesi:", kesisim)

# Fark kümesi (A - B)
fark_AB = A.difference(B)
print("A - B Fark Kümesi:", fark_AB)

# Fark kümesi (B - A)
fark_BA = B.difference(A)
print("B - A Fark Kümesi:", fark_BA)

# Simetrik fark kümesi
simetrik_fark = A.symmetric_difference(B)
print("Simetrik Fark Kümesi:", simetrik_fark)

# Birleşim Kümesi: {1, 2, 3, 4, 5, 6, 7, 8}
# Kesişim Kümesi: {4, 5}
# A - B Fark Kümesi: {1, 2, 3}
# B - A Fark Kümesi: {8, 6, 7}
# Simetrik Fark Kümesi: {1, 2, 3, 6, 7, 8}


