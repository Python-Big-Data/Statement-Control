# Tinjau kembali kode program pada nomor 5 di atas. Modifikasilah kode programnya sehingga diperoleh tampilan seperti
# gambar 5.12
# * * * * *
# * * * *
# * * *
# * *
# *

# Ini untuk kolom
i = "* "
for i in range(5):
    # Ini untuk baris
    for j in range(5 - i):
        print("* ", end="")

    print("\n")

