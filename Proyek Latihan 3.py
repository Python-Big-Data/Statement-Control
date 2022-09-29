# 3. Buatlah kode program Python untuk menentukan gaji pokok dan gaji bersih dari seorang karyawan berdasarkan
# golongannya. Berikut ini adalah aturan perhitungan hgaji pokoknya:


# Data-Data
A = 10000000
B = 8500000
C = 7000000
D = 5000000

potA = 0.025
potB = 0.02
potC = 0.015
potD = 0.01

# Logics
x = 'Y'
while x == 'Y':
    kodeKaryawan = int(input('Masukkan kode karyawan      : '))
    namaKaryawan = input('Masukkan nama karyawan      : ')
    golongan = input('Masukkan golongan           : ')
    if golongan == 'A':
        print('==============================================')
        print('STRUK RINCIAN GAJI KARYAWAN')
        print('----------------------------------------------')
        print('Nama Karyawan               : ', namaKaryawan, '(Kode: ', kodeKaryawan, ')')
        print('Golongan                    : ', golongan)
        print('----------------------------------------------')
        print('Gaji Pokok                  :', 'Rp', A)
        print('Potongan (', potA, '(%))       :', 'Rp', int(A * potA))
        print('----------------------------------------------')
        print('Gaji Bersih                 : Rp', int(A - (A * potA)))

    elif golongan == 'B':
        print('==============================================')
        print('STRUK RINCIAN GAJI KARYAWAN')
        print('----------------------------------------------')
        print('Nama Karyawan              : ', namaKaryawan, '(Kode: ', kodeKaryawan, ')')
        print('Golongan                   : ', golongan)
        print('----------------------------------------------')
        print('Gaji Pokok                 :', 'Rp', B)
        print('Potongan (', potB, '(%))       :', 'Rp', int(A * potB))
        print('----------------------------------------------')
        print('Gaji Bersih                : Rp', int(B - (B * potB)))
    elif golongan == 'C':
        print('==============================================')
        print('STRUK RINCIAN GAJI KARYAWAN')
        print('----------------------------------------------')
        print('Nama Karyawan              : ', namaKaryawan, '(Kode: ', kodeKaryawan, ')')
        print('Golongan                   : ', golongan)
        print('----------------------------------------------')
        print('Gaji Pokok                 :', 'Rp', C)
        print('Potongan (', potC, '(%))      :', 'Rp', int(C * potC))
        print('----------------------------------------------')
        print('Gaji Bersih                : Rp', int(C - (C * potC)))
    elif golongan == 'D':
        print('==============================================')
        print('STRUK RINCIAN GAJI KARYAWAN')
        print('----------------------------------------------')
        print('Nama Karyawan              : ', namaKaryawan, '(Kode: ', kodeKaryawan, ')')
        print('Golongan                   : ', golongan)
        print('----------------------------------------------')
        print('Gaji Pokok                 :', 'Rp', D)
        print('Potongan (', potD, '(%))      :', 'Rp', int(D * potD))
        print('----------------------------------------------')
        print('Gaji Bersih                : Rp', int(D - (D * potD)))
    x = input("Apakah Anda ingin mengulanginya ? (Y/N)")
    if x == "Y" or "y":
        continue
    print(x)