# Buatlah game tebak angka dengan seknario sebagai berikut.
# Komputer akan memilih sebuah bilangan bulat secara random, antara 0 s/d 100
# Bilangan tersebut tersimpan dalam memori komputer
# Tugas pemain adalah menebak bilangan yang dipilih komputer tersebut.
# Untuk menebak bilangan, pemain mengentri beberapa bilangan
# Komputer memberikan respon 'Bilangan tebakan Anda terlalu besar' jika bilangan yang dientri pemain lebih besar
# dari bilangan yang dipilih komputer atau 'Bilangan tebakan Anda terlalu kecil' jika bilangan yang di entri pemain
# lebih kecil dari bilangan yang dipilih komputer adalah 10;

# Hai.. nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100.
# Silakan tebak ya!!!"
# Tebakan Anda: 4
# hehehe.. Bilangan tebakan Anda terlalu kecil
# Tebakan Anda: 20
# hehehe.. Bilangan tebakan Anda terlalu besar
# Tebakan Anda: 15
# hehehe.. Bilangan tebakan Anda terlalu besar
# Tebakan Anda: 9
# hehehe.. Bilangan tebakan Anda terlalu kecil
# Tebakan Anda: 10
# yeeee.. Bilangan tebakan Anda BENAR :-)

# Game tebakan
namaPemain = input("Masukkan nama pemain: ")
print("Hai.. nama saya", namaPemain, ", saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. ")
print("Silakan tebak ya!!!")
jawaban = 10
while True:
    tebakan = int(input("Tebakan Anda: "))
    jawaban = 10
    if tebakan == 10:
        print("yeeee.. Bilangan tebakan Anda BENAR :-)")
        break
    elif tebakan <= 10:
        print("hehehe.. Bilangan tebakan Anda terlalu kecil")
        tebakan != 10
    else:
        print("hehehe.. Bilangan tebakan Anda terlalu besar")
        tebakan != 10











