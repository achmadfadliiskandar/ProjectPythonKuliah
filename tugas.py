def fungsi():
    print("Aplikasi Kelas 1IA04 app\n")
    # tugas 1 Perhitungan 
    # penentuan angka Ganjil dan Genap
    # tugas 2 
    # Perhitungan penentuan angka Negatif dan Positif.
    # tugas 3 Penentuan Deret Hari
    # tugas 4 Penentuan Deret Bulan

    print("menu aplikasi")
    print("1.Perhitungan penentuan angka Ganjil dan Genap")
    print("2.Perhitungan penentuan angka Negatif dan Positif")
    print("3 Penentuan Deret Hari")
    print("4 Penentuan Deret Bulan")
    print("5 Keluar\n")

    option = int(input("masukan pilihan yang ada di atas ya : "))

    # ini pilihan 1
    if option == 1:
        datainput = int(input("Masukan Angka yang ingin di tentukan : "))
        if datainput % 2:
            print("Ganjil")
        elif datainput == 0:
            print('Nilainya Jangan 0 ya\nnggak kehitung')
        else:
            print("Genap")
        while True:
            datakonfirmasi = input("mau main lagi nggak ? ")
            if datakonfirmasi == "y":
                datainput = int(input("Masukan Angka yang ingin di tentukan : "))
                if datainput % 2:
                    print("Ganjil")
                elif datainput == 0:
                    print('Nilainya Jangan 0 ya\nnggak kehitung')
                else:
                    print("Genap")
            elif datakonfirmasi == "n":
                print("terima kasih sudah mencoba")
                # exit()
                return fungsi()
            else:
                print('maaf cuma ada 2 menu diatas ya')
                print('pilih yang benar ya !!')
                continue
    # akhir pilihan 1

    # ini pilihan 2
    elif option == 2:
        tulisanpn = int(input("Masukan Angka yang ingin di tentukan : "))
        if tulisanpn > 0:
            print("Positif")
        else:
            print("Negatif")
        while True:
            datakonfirmasi = input("mau main lagi nggak ? ")
            if datakonfirmasi == "y":
                tulisanpn = int(input("Masukan Angka yang ingin di tentukan : "))
                if tulisanpn > 0:
                    print("Positif")
                else:
                    print("Negatif")
            elif datakonfirmasi == "n":
                print("terima kasih sudah mencoba")
                return fungsi()
                # exit()
            else:
                print('maaf cuma ada 2 menu diatas ya')
                print('pilih yang benar ya !!')
                continue
    # akhir pilihan 2

    # ini pilihan 3
    elif option == 3:
        hari = ['senin','selasa','rabu','kamis','jumat','sabtu','minggu']
        inputhari = int(input("Masukan Angka 1 - 7 : "))-1
        if inputhari < 0:
            print('kurang ya hanya 1-7 aja')
        elif inputhari < 7:
            print('Hari Ini Hari ',hari[inputhari])
        else:
            print('kelewatan ya hanya 1-7 aja')
        while True:
            datakonfirmasi = input("mau main lagi nggak ? ")
            if datakonfirmasi == "y":
                inputhari = int(input("Masukan Angka 1 - 7 : "))-1
                if inputhari < 0:
                    print('kurang ya hanya 1-7 aja')
                elif inputhari < 7:
                    print('Hari Ini Hari ',hari[inputhari])
                else:
                    print('kelewatan ya hanya 1-7 aja')
            elif datakonfirmasi == "n":
                print("terima kasih sudah mencoba")
                return fungsi()
                # exit()
            else:
                print('maaf cuma ada 2 menu diatas ya')
                print('pilih yang benar ya !!')
                continue
    # akhir pilihan 3

    # ini pilihan 4
    elif option == 4:
        bulan = ['januari','februari','maret','april','mei','juni','juli','agustus','september','oktober','november','desember']
        inputbulan = int(input("Masukan Angka 1 - 12 : "))-1
        if inputbulan < 0:
            print('kurang ya hanya 1-12 aja')
        elif inputbulan < 12:
            print('bulan Ini bulan ',bulan[inputbulan])
        else:
            print('kelewatan ya hanya 1-12 aja')
        while True:
            datakonfirmasi = input("mau main lagi nggak ? ")
            if datakonfirmasi == "y":
                inputbulan = int(input("Masukan Angka 1 - 12 : "))-1
                if inputbulan < 0:
                    print('kurang ya hanya 1-12 aja')
                elif inputbulan < 12:
                    print('bulan Ini bulan ',bulan[inputbulan])
                else:
                    print('kelewatan ya hanya 1-12 aja')
            elif datakonfirmasi == "n":
                print("terima kasih sudah mencoba")
                return fungsi()
                # exit()
            else:
                print('maaf cuma ada 2 menu diatas ya')
                print('pilih yang benar ya !!')
                continue
    # akhir pilihan 4
            
    # pilihan 5
    if option == 5:
        print("terima kasih sudah mencoba aplikasi ini")
        exit()
    # akhir pilihan 5

    # kalau pilihan nya nggak ada dan nggak sesuai 
    # ya kesini aja wkwk
    else:
        print('nggak ada pilihan nya ya')
        return fungsi()
    # kalau pilihan nya nggak ada dan nggak sesuai 
    # ya kesini aja wkwk
fungsi()