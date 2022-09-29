# Buatlah kode program Python untuk men-generate syair lagu'anak ayam ' sebagi berikut.
# Anak ayam turun 3 mati satu tinggalah . Anak ayam turun 2, mati satu tinggalah 1. Anak ayam turun 1, mati satu tinggal
# induknya
# Adapun jumlah ayam mula-mula adalah n buah yang merupakan input program. Contoh syair anak ayam di atas adalah
# untuk n = 3.

# Kita akan memberikan sebuah input n :
n = int(input("Masukkan jumlah anak ayam mula-mula: "))

while n >= 1:
    if n > 1:
        print("Anak ayam turun", n, ", mati satu tinggalah", n - 1)
    else:
        print("Anak ayam turun", n, ", mati satu tinggal induknya")
    n = n - 1
