print("program looping python")
tanyain_dlu = int(input("batas inputnya mau brp ? "))
batas_tanya = tanyain_dlu + 1
for i in range(batas_tanya):
    satu = input(f"kalimat {i + 1} : ")
    dua = input(f"kalimat {i + 1} : ")
    # print('jumlah kalimat jadi  : ', i+1)
    print(f'kalimat yang dikumpulkan di Kalimat {i}  jadi ? : ', satu + dua)