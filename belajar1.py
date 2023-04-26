jari2 = int(input("masukan nilai Luas Lingkaran : "))
keliling = int(input("masukan nilai Keliling Lingkaran : "))
rumus = 3.14 * jari2 * jari2
hasil = print(rumus,"cm")
rumuskeliling = 2 *3.14 * keliling
print(rumuskeliling,"cm")

# jika nilai diatas 60 maka lulus dan 60 juga lulus

masukan_nilai = float(input("masukan nilai : "))


if masukan_nilai <= 100:
    if masukan_nilai < 0:
        print('nilainya jangan kurang dari 0 ya')
    if masukan_nilai < 60:
        print('anda tidak lulus')
    else:
        print('anda lulus')
else:
    print('dilarang lebih dari 100')