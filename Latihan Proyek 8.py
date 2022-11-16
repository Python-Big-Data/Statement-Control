# Modifikasilah program nomor 7 sehingga bisa menampilkan score pemain. Berikut ini aturan perhitungan scorenya:
# Mula-mulascroe pemain adalah 100 poin
# setiap kali tebakan pemain salah, maka skornya berkurang 2 poin
# Score minimal pemain adalah 0 (score negatif tidak diperbolehkan)
# Contoh tampilan misalkan bilangan yang dipilih komputer adalah 10:
# "Hai.. nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100.
# Silahkan tebak saya!!!"

# Tebakan Anda: 4
# hehehe.. Bilangan tebakan Anda terlalu kecil
# Tebakan Anda: 20
# hehehe.. Bilangan tebakan Anda terlalu kecil
# Tebakan Anda: 15
# hehehe.. Bilangan tebakan Anda terlalu kecil
# Tebakan Anda: 9
# hehehe.. Bilangan tebakan Anda terlalu kecil
# Tebakan Anda: 10
# Yeeee.. Bilangan tebakan Anda BENAR :-)
# Score Anda : 92
# Game tebakan
namaPemain = input("Masukkan nama pemain: ")
print("Hai.. nama saya", namaPemain, ", saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. ")
print("Silakan tebak ya!!!")
poinAwal = 100
jawaban = 10
while True:
    score = poinAwal - 2
    if score == 0:
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
    else:
        print("Anda kalah")
        break

print(f"Score Anda: {score}")