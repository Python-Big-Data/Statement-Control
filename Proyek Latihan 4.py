# 4. Modifikasikanlah kode program yang dihasilakan dari nomor 3, apabila dalam perhitungan gaji
# terdapat tunjangan-tunjangan sebagai berikut:
#     Tunjangan istri/suami : 10% dari gaji pokok (jika statusnya menikah).
#     Tunjangan anak : 5% dari gaji pokok untuk setiap anak (jika memiliki anak) dan statusnya menikah.
# Adapun rumus untuk menghitung gaji bersih adalah sebagai berikut:
#     Gaji Kotor = Gaji Pokok  + Tunjangan Istri/Suami + Tunjangan anak
#     Gaji Bersih = Gaji Kotor - Potongan
# Keterengan:
# Perhitungan potongan dilakukan terhadap gaji kotor, yang besar % nya menyesuaikan golongan karyawan.


# Logics
x = 'Y'
while x == 'Y':
    kodeKaryawan = int(input('Masukkan kode karyawan      : '))
    namaKaryawan = input('Masukkan nama karyawan      : ')
    golongan = input('Masukkan golongan           : ')
    status = input('Masukkan status (1: Menikah, 2: blm)           : ')
    if status == 1:
        anak = input('Masukkan jumlah anak           : ')
    else:
        if golongan == 'A':
            print('==============================================')
            print('STRUK RINCIAN GAJI KARYAWAN')
            print('----------------------------------------------')
            print('Nama Karyawan               : ', namaKaryawan, '(Kode: ', kodeKaryawan, ')')
            print('Golongan                    : ', golongan)
            print('Status menikah                    : ', status)
            print('Jumlah anak                    : ', anak)
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