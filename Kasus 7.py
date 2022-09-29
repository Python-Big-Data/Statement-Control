# Buatlah program untuk menampilkan semua bilangan yang habis dibagi 3 dan 5 antara 1 sampai 100, kemudian hitung
# banyaknya bilangan, serta hitung pula jumlahan semua bilangan tersebut.

# Berikut ini adalah codenya
# kita definisikan dahulu masing-masing
banyakBilangan = 0
jumlahBilangan = 0
for i in range (100):
    bil = i + 1
    if (bil % 3) == 0 and  (bil % 5) == 0:
        # ini untuk menghitung banyaknya bilangan yang ada
        banyakBilangan +=1
        # ini untuk menghitung jumlahan semua bilangan tersebut
        sukuBilangan = i + 1
        jumlahBilangan = jumlahBilangan + sukuBilangan
print("Maka banyaknya bilangan tersebut adalah " + str(banyakBilangan) + " bilangan")
print("Jumlahan dari bilanga-bilangan tersebut adalah " + str(jumlahBilangan) + " bilangan")