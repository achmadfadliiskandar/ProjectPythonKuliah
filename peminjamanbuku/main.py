print("Peminjaman Buku")

datamenu = [
    "1.Lihat Data Buku",
    #1. lihat data buku yang tersedia
    "2.Lihat Data Peminjam",
    #2. lihat data orang yang meminjam (orangnya aja)
    "3.Cari Data Peminjam",
    #3. cari data orang yang meminjam + bukunya apa? 
    "4.Cari Data Buku",
    #4. cari detail data buku (tahun, seri, penerbit)
    "5.Pinjam buku",
    #5. minjam buku apa
    "6.Kembalikan buku",
    #6. membalikan buku apa
    "7.Keluar"
    #7. biar user bisa keluar dari aplikasi
]
for i in datamenu:
    print(str.upper(i))

# membuat fungsi 
def menu():
    while True:
        try:
            keymenu = int(input("Masukan Menu Yang Tertera : "))
        except:
            print("Isinya menunya jangan huruf atau simbol")
            continue
        else:
            # print("kamu nanya!!!")
            if keymenu == 1:
                def showbuku():
                    f = open("peminjamanbuku/buku.txt",'r')
                    print(f.read())
                showbuku()
                menu_input = input("Keluar Tekan Enter Ya ....")
                if menu_input != False:
                    return menu()
            elif keymenu == 2:
                def seepeople():
                    pem = open("peminjamanbuku\peminjam.txt","r")
                    print(pem.read())
                seepeople()
                menu_input = input("Keluar Tekan Enter Ya ....")
                if menu_input != False:
                    return menu()
            elif keymenu == 3:
                def menupeminjam():
                    searchview = str(input("masukan Nama Peminjam : ")).capitalize()
                    with open(r'peminjamanbuku\detailpeminjam.txt','r') as file:
                        content = file.readlines()
                        for isi in content:
                            if isi.find(searchview) != -1:
                                print('Tersedia Pencarian',searchview)
                                print("isi Konten : ",content.index(isi))
                                print("baris",isi)
                menupeminjam()
                menu_input = input("Keluar Tekan Enter Ya ....")
                if menu_input != False:
                    return menu()
            elif keymenu == 4:
                def detailbuku():
                    pencarianbuku = str(input("masukan Buku Yang Dicari : ")).capitalize()
                    with open(r'peminjamanbuku\detailbuku.txt','r') as file:
                        content = file.readlines()
                        for isi in content:
                            if isi.find(pencarianbuku) != -1:
                                print('Tersedia Pencarian',pencarianbuku)
                                print("isi Konten : ",content.index(isi))
                                print("baris",isi)
                detailbuku()
                menu_input = input("Keluar Tekan Enter Ya ....")
                if menu_input != False:
                    return menu()
            elif keymenu == 5:
                filename = "peminjamanbuku/buku.txt"
                with open(filename) as f:
                    data = f.read()
                namapeminjam = input("masukan nama Anda : ")
                namabuku = input("masukan nama buku yang ingin anda pinjamkan : ")
                tanggal_pinjam = input("masukan tanggal Pinjam :  ")
                if namabuku in data:
                    c = open('peminjamanbuku\detailpeminjam.txt')
                    d = c.read()
                    if namabuku in d:
                        print('buku sudah terpinjam')
                    else:
                        text = "\nNama : {},Buku : {},Tanggal Pinjam Y-m-d : {} ".format(namapeminjam,namabuku,tanggal_pinjam)
                        f = open("peminjamanbuku\detailpeminjam.txt","a")
                        f.write(text)
                        f.close()
                    # f.write("\nNama : "+namapeminjam+",Buku : "+namabuku)
                    # print("Nama Buku Yang dipinjam : " + namabuku)
                else:
                    print('buku tidak tersedia')
                menu_input = input("Keluar Tekan Enter Ya ....")
                if menu_input != False:
                    return menu()
            elif keymenu == 6:
                buka = open("peminjamanbuku\detailpeminjam.txt","r")
                data = buka.readlines()
                # print(data)
                if data == 0:
                    print('nggak ada data peminjam yang terdaftar')
                else:
                    for i,j in enumerate(data,start=0):
                        print(i,j,"\n")
                # menampilkan data
                index = int(input("Isi Index Detail Peminjamnya : "))
                # print(data[index])
                # append
                f = open("peminjamanbuku\pengembalian.txt","a")
                f.write(data[index])
                f.close()
                # read
                f = open("peminjamanbuku\pengembalian.txt", "r")
                print(f.read())

                # hapus file peminjaman setelah berhasil menambahkan ke pengembalian
                data_file  = open("peminjamanbuku\detailpeminjam.txt",'r')
                lines = data_file.readlines()
                data_file.close()

                write_file = open("peminjamanbuku\detailpeminjam.txt",'w')
                for line in lines:
                    if data[index] not in line:
                        write_file.write(line)
                write_file.close()
                read_file = open("peminjamanbuku\detailpeminjam.txt",'r')
                lines = read_file.readlines()
                read_file.close()
                for line in lines:
                    print(line)
                menu_input = input("Keluar Tekan Enter Ya ....")
                if menu_input != False:
                    return menu()
            elif keymenu == 7:
                exit()
            else:
                print("menu nggak ada")
                continue
        break
menu()   