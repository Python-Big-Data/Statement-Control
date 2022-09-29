# 1. Buatlah kode program dengan Python untuk menentukan status kelulusan ujian mahasiswa. Syarat kelulusan adalah:
# - Tidak ada nilai yang kurang dari 60, dan
# - Nilai matematikanya harus di atas 70
# Keterangan :
# - Input berupa nilai-nilai mata pelajaran : bhs Indonesia, matematika, ipa
# - Range input nilai adalah 0 - 100 (apabila nilai yang diinputkan di luar dari range ini maka akan muncul pesan
# peringatan)
# Contoh hasil output tampilan program yang diharapkan:
# Masukkan nilai Bhs Indonesia : 50
# Masukkan nilai IPA           : 70
# Masukkan nilai Matematika    : 80
# Status Kelulusan             : TIDAK LULUS


# input nilai pelajaran
nilaiBhsIndonesia = int(input("Masukkan nilai Bahasa Indonesia: "))
nilaiMatematika = int(input("Masukkan nilai Matematika      : "))
nilaiIpa = int(input("Masukkan nilai IPA             : "))

while True:
    if nilaiBhsIndonesia <= 100 and nilaiIpa <= 100 and nilaiMatematika <= 100:
        if nilaiBhsIndonesia > 60 and nilaiIpa > 60 and nilaiMatematika > 70:
            print("Status Kelulusan               : LULUS")
            break
        else:
            print("Status Kelulusan               : TIDAK LULUS")
            break
    else:
        print("Peringatan: Nilai yang dimasukkan harus di bawah 100")
        break

