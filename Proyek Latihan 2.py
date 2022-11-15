# 2. Modifikasilah kode program yang sudah dibuat pada soal nomor 1, sehingga menampilkan sebab ketidaklulusannya
# pada output program.
# Contoh hasil output tampilan program yang diharapkan:
# Masukkan nilai Bhs Indonesia : 50
# Masukkan nilai IPA           : 70
# Masukkan nilai Matematika    : 40
# Masukkan Kelulusan           : TIDAK LULUS
# Sebab                        :
# - Nilai bahasa Indonesia kurang dari 60
# - Nilai matematikanya kurang dari 70


# Perubahan kedua
# input nilai pelajaran
nilaiBhsIndonesia = int(input("Masukkan nilai Bahasa Indonesia: "))
nilaiMatematika = int(input("Masukkan nilai Matematika      : "))
nilaiIpa = int(input("Masukkan nilai IPA             : "))

while True:
    if nilaiBhsIndonesia <= 100 and nilaiIpa <= 100 and nilaiMatematika <= 100:
        if nilaiBhsIndonesia > 60 and nilaiIpa > 60 and nilaiMatematika > 70:
            statusKelulusan = input("Masukkan Kelulusan             : ")
            if statusKelulusan == "LULUS" or statusKelulusan == "lulus" or statusKelulusan == "Lulus":
                print("Sebab                          : \n - Nilai bahasa Indonesia lebih dari 60 \n - Nilai matematikanya lebih dari 70 ")
            break
        else:
            statusKelulusan = input("Masukkan Kelulusan             : ")
            if statusKelulusan == "TIDAK LULUS" or statusKelulusan == "tidak lulus" or statusKelulusan == "tidak":
                print(
                    "Sebab                          : Nilai bahasa Indonesia kurang dari 60 dan Nilai matematikanya kurang dari 70")

            break
    else:
        print("Peringatan: Nilai yang dimasukkan harus di bawah 100")
        break

