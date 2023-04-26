print("Aplikasi Tabel Perkalian")

angkayangdikali = int(input("Masukan Angka yang ingin dikali : "))
pengkalinya = int(input("Masukan Angka Pengkalinya  : "))
print("Angka yang akan dijumlah : ",pengkalinya,"*",angkayangdikali)

for i in range(angkayangdikali,pengkalinya):
    print(i * pengkalinya,"*",angkayangdikali," = ",pengkalinya*i)