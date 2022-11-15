# 4. Modifikasikanlah kode program yang dihasilakan dari nomor 3, apabila dalam perhitungan gaji
# terdapat tunjangan-tunjangan sebagai berikut:
#     Tunjangan istri/suami : 10% dari gaji pokok (jika statusnya menikah).
#     Tunjangan anak : 5% dari gaji pokok untuk setiap anak (jika memiliki anak) dan statusnya menikah.
# Adapun rumus untuk menghitung gaji bersih adalah sebagai berikut:
#     Gaji Kotor = Gaji Pokok  + Tunjangan Istri/Suami + Tunjangan anak
#     Gaji Bersih = Gaji Kotor - Potongan
# Keterangan:
# Perhitungan potongan dilakukan terhadap gaji kotor, yang besar % nya menyesuaikan golongan karyawan.


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
    status = input('Masukkan status (1: Menikah, 2: Belum Menikah )           : ')
    if status == "menikah" or status == "Menikah" or status == "MENIKAH":
        anak = int(input('Masukkan jumlah anak        : '))
        tunjanganIstriSuami = float(0.1 * A)
        tunjanganAnak = float(A * 0.05 * anak)
        gajiKotor = A + tunjanganIstriSuami + tunjanganAnak
        if golongan == 'A':
            print('==============================================')
            print('STRUK RINCIAN GAJI KARYAWAN')
            print('----------------------------------------------')
            print('Nama Karyawan               : ', namaKaryawan, '(Kode: ', kodeKaryawan, ')')
            print('Golongan                    : ', golongan)
            print('Status menikah              : ', status)
            print('Jumlah anak                 : ', anak)
            print('----------------------------------------------')
            print('Gaji Pokok                  :', 'Rp', A)
            print('Tunjangan Istri dan Suami   :', 'Rp', tunjanganIstriSuami)
            print('Tunjangan anak              :', 'Rp', tunjanganAnak)
            print('Potongan (', potA, '(%))       :', 'Rp', float(gajiKotor * potA))
            print('----------------------------------------------')
            print('Gaji Bersih                 : Rp', float(gajiKotor - (gajiKotor * potA)))

        elif golongan == 'B':
            print('==============================================')
            print('STRUK RINCIAN GAJI KARYAWAN')
            print('----------------------------------------------')
            print('Nama Karyawan               : ', namaKaryawan, '(Kode: ', kodeKaryawan, ')')
            print('Golongan                    : ', golongan)
            print('Status menikah              : ', status)
            print('Jumlah anak                 : ', anak)
            print('----------------------------------------------')
            print('Gaji Pokok                  :', 'Rp', B)
            print('Tunjangan Istri dan Suami   :', 'Rp', tunjanganIstriSuami)
            print('Tunjangan anak              :', 'Rp', tunjanganAnak)
            print('Potongan (', potB, '(%))        :', 'Rp', float(gajiKotor * potB))
            print('----------------------------------------------')
            print('Gaji Bersih                 : Rp', float(gajiKotor - (gajiKotor * potB)))
        elif golongan == 'C':
            print('==============================================')
            print('STRUK RINCIAN GAJI KARYAWAN')
            print('----------------------------------------------')
            print('Nama Karyawan               : ', namaKaryawan, '(Kode: ', kodeKaryawan, ')')
            print('Golongan                    : ', golongan)
            print('Status menikah              : ', status)
            print('Jumlah anak                 : ', anak)
            print('----------------------------------------------')
            print('Gaji Pokok                  :', 'Rp', C)
            print('Tunjangan Istri dan Suami   :', 'Rp', tunjanganIstriSuami)
            print('Tunjangan anak              :', 'Rp', tunjanganAnak)
            print('Potongan (', potC, '(%))       :', 'Rp', float(gajiKotor * potC))
            print('----------------------------------------------')
            print('Gaji Bersih                 : Rp', float(gajiKotor - (gajiKotor * potC)))
        elif golongan == 'D':
            print('==============================================')
            print('STRUK RINCIAN GAJI KARYAWAN')
            print('----------------------------------------------')
            print('Nama Karyawan               : ', namaKaryawan, '(Kode: ', kodeKaryawan, ')')
            print('Golongan                    : ', golongan)
            print('Status menikah              : ', status)
            print('Jumlah anak                 : ', anak)
            print('----------------------------------------------')
            print('Gaji Pokok                  :', 'Rp', D)
            print('Tunjangan Istri dan Suami   :', 'Rp', tunjanganIstriSuami)
            print('Tunjangan anak              :', 'Rp', tunjanganAnak)
            print('Potongan (', potD, '(%))        :', 'Rp', float(gajiKotor * potD))
            print('----------------------------------------------')
            print('Gaji Bersih                 : Rp', float(gajiKotor - (gajiKotor * potD)))
    elif status == "belum menikah" or status == "Belum Menikah" or status == "BELUM MENIKAH":
        anak = "nil"
        tunjanganIstriSuami = "nil"
        tunjanganAnak = "nil"
        if golongan == 'A':
            print('==============================================')
            print('STRUK RINCIAN GAJI KARYAWAN')
            print('----------------------------------------------')
            print('Nama Karyawan               : ', namaKaryawan, '(Kode: ', kodeKaryawan, ')')
            print('Golongan                    : ', golongan)
            print('Status menikah              : ', status)
            print('Jumlah anak                 : ', anak)
            print('----------------------------------------------')
            print('Gaji Pokok                  :', 'Rp', A)
            print('Tunjangan Istri dan Suami   :', 'Rp', tunjanganIstriSuami)
            print('Tunjangan anak              :', 'Rp', tunjanganAnak)
            print('Potongan (', potA, '(%))       :', 'Rp', int(A * potA))
            print('----------------------------------------------')
            print('Gaji Bersih                 : Rp', int(A - (A * potA)))

        elif golongan == 'B':
            print('==============================================')
            print('STRUK RINCIAN GAJI KARYAWAN')
            print('----------------------------------------------')
            print('Nama Karyawan               : ', namaKaryawan, '(Kode: ', kodeKaryawan, ')')
            print('Golongan                    : ', golongan)
            print('Status menikah              : ', status)
            print('Jumlah anak                 : ', anak)
            print('----------------------------------------------')
            print('Gaji Pokok                  :', 'Rp', B)
            print('Tunjangan Istri dan Suami   :', 'Rp', tunjanganIstriSuami)
            print('Tunjangan anak              :', 'Rp', tunjanganAnak)
            print('Potongan (', potB, '(%))    :', 'Rp', int(B * potB))
            print('----------------------------------------------')
            print('Gaji Bersih                 : Rp', int(B - (B * potB)))
        elif golongan == 'C':
            print('==============================================')
            print('STRUK RINCIAN GAJI KARYAWAN')
            print('----------------------------------------------')
            print('Nama Karyawan               : ', namaKaryawan, '(Kode: ', kodeKaryawan, ')')
            print('Golongan                    : ', golongan)
            print('Status menikah              : ', status)
            print('Jumlah anak                 : ', anak)
            print('----------------------------------------------')
            print('Gaji Pokok                  :', 'Rp', C)
            print('Tunjangan Istri dan Suami   :', 'Rp', tunjanganIstriSuami)
            print('Tunjangan anak              :', 'Rp', tunjanganAnak)
            print('Potongan (', potC, '(%))    :', 'Rp',int(C * potC))
            print('----------------------------------------------')
            print('Gaji Bersih                 : Rp', int(C - (C * potC)))
        elif golongan == 'D':
            print('==============================================')
            print('STRUK RINCIAN GAJI KARYAWAN')
            print('----------------------------------------------')
            print('Nama Karyawan               : ', namaKaryawan, '(Kode: ', kodeKaryawan, ')')
            print('Golongan                    : ', golongan)
            print('Status menikah              : ', status)
            print('Jumlah anak                 : ', anak)
            print('----------------------------------------------')
            print('Gaji Pokok                  :', 'Rp', D)
            print('Tunjangan Istri dan Suami   :', 'Rp', tunjanganIstriSuami)
            print('Tunjangan anak              :', 'Rp', tunjanganAnak)
            print('Potongan (', potD, '(%))    :', 'Rp', int(D * potD))
            print('----------------------------------------------')
            print('Gaji Bersih                : Rp', int(D - (D * potD)))

    x = input("Apakah Anda ingin mengulanginya ? (Y/N)")
    if x == "Y" or "y":
        continue
    print(x)