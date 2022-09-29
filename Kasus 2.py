# Buatlah sebuah program untuk menjumlahkan dua buah bilangan bulat yang berasal dari input.
# Setiap kali setelah menampilkan hasil penjumlahannya, tampilkan pertanyaan (Y/N) apakah user ingin
# mengulanginya lagi (menjumlahkan untuk bilangan lainnya). Jika user memilih Y, maka program meminta user
# memasukkan kembali kedua bilnagan yang akan dijumlahkan, kemudian program menampilkan hasilnya.
# Namun jika user memilih N, maka program berhenti.


while True:
    # Masukkan 2 angka yang ingin diinput
    angkaPertama = int(input("Masukkan bilangan bulat pertama: "))
    angkaKedua = int(input("Masukkan bilangan bulat kedua: "))

    # Proses
    hasilPenjumlahan = angkaPertama + angkaKedua
    print("Maka hasil penjumlahan dari bilangan pertam dan kedua adalah ", hasilPenjumlahan)
    x = input("Apkah user ingin mengulanginya (menjumlahkan untuk bilangan lainnya)? (Y/N)")
    if x == "N" or "n":
        break