# Buatlah program untuk menghitung hasil dari 1 + 2 + 3 + ... + 100.

sum1 = 0
for i in range (100):
    suku = i + 1
    sum1 = sum1 + suku
print("Hasil penjumlahannya adalah " + str(sum1))
