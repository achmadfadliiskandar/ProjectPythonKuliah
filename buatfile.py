import pandas as pds
excel_data = pds.read_excel("coba.xlsx")
open_file = pds.DataFrame(excel_data,columns=['no','univ','kampus','kelas'])
print("Hasil Di bawah Ini adalah : \n",open_file)
# cara untuk menghapus file
# jika ingin menghapus
# import os
# os.remove("satu.txt")

# cara untuk membuat file
# metode Create
# print("membuat file")
# x = open("satu.txt","x")
# x.write("sudah saya buat filenya")
# x.close()

# metode Write
# f = open("demofile3.txt", "w")
# f.write("aku sudah membuat konten nya")
# f.close()



# membaca file
# metode read
# f = open("demofile3.txt", "r")
# print(f.read())
# # metode readline
# g = open("satu.txt", "r")
# print(g.readline())