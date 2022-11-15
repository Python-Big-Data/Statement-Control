# Buatlah program python untuk menampilkan bilangan bulat dari 0 sampai dengan 100 yang ganjil.
# Lengkapi juga dengan menampilkan banyaknya bilangan bulat dari 0 sampai 100 yang ganjil dan tampilkan juga total
# jumlahan seleuruh bilangan ganjil ( 1 + 3 + 5 + .. ).
# Contoh hasil output :
# 1
# 3
# 5
# 7
#.
#.
# dst
# Banyaknya bilangan ganjil : xxx
# Jumlah seluruh bilangan ganjil : xxx
# Banyaknya  bilangan ganjil : xxx

# Program bialangan bulat dari 0 sampai 100 yang ganjil
sum1 = 0
for i in range(1, 100, 2):
    suku = i
    sum1 = sum1 + suku
# Print nya harus diluar dari scopenya
print("Hasil penjumlahannya adalah " + str(sum1))

