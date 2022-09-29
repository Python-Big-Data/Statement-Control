# Buatlah program Python untuk mengkonversi nilai angka 0-100 ke dalam nilai huruf dengan ketentuan seperti berikut:

# Program akan mengkonversi nilai yang ada ke dalam huruf yang sudah disediakan
# Masukkan User Input
masukAngka = int(input("Masukkan angka yang diinginkan: "))

# Karena dalam Python tidak ada switch maka kita akan menggunakan if else
# Code berikut akan menafsirkan huruf yang ada ke dalam huruf
if masukAngka >= 80 and masukAngka <= 100:
    print("Maka nilai hurufnya akan menjadi A")
elif masukAngka >= 70 and masukAngka <= 79:
    print("Maka nilai hurufnya akan menjadi B")
elif masukAngka >= 60 and masukAngka <= 69:
    print("Maka nilai hurufnya akan menjadi C")
elif masukAngka >= 40 and masukAngka <= 59:
    print("Maka nilai hurufnya akan menjadi D")
elif masukAngka >= 0 and masukAngka <= 39:
    print("Maka nilai hurufnya akan menjadi E")
else:
    print("Masukkan angka di antara 0 - 100")
