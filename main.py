# Program Peminjaman Buku Perpustakaan

# List
daftar_buku = [
    {'judul': 'Harry Potter and the Sorcerers Stone',
        'tahun': 1997, 'penerbit': 'Bloomsbury'},
    {'judul': 'Si Putih', 'tahun': 2021, 'penerbit': 'Tere Liye'},
    {'judul': 'Bumi Manusia', 'tahun': 1980, 'penerbit': 'Pramoedya Ananta Toer'},
    {'judul': 'Pendidikan Karakter', 'tahun': 2011, 'penerbit': 'Samudra Biru'},
    {'judul': 'Menjadi Guru Idola', 'tahun': 2005 , 'penerbit': 'Pustaka Inti'},
    {'judul': 'Mengukir Prestasi', 'tahun': 2002, 'penerbit': 'Misaka Galiza'},
    {'judul': 'Menghadapi Anak di Saat Sulit', 'tahun': 2004, 'penerbit': 'DELAPRATASA Publishing'}
]

file_txt = 'peminjam.txt'


def main():
    while True:
        # Menampilkan Menu
        print('Menu Peminjaman Buku Perpustakaan:')
        print('1. Cari Peminjam')
        print('2. Cari Buku')
        print('3. Pinjam Buku')
        print('4. Kembalikan Buku')
        print('5. Lihat Data Peminjam')
        print('6. Lihat List Buku')
        print('7. Keluar Menu')

        pilihan = input('Pilih menu: ')

        # Percabangan
        if pilihan == '1':
            cari_peminjam()
        elif pilihan == '2':
            cari_buku(daftar_buku)
        elif pilihan == '3':
            pinjam_buku()
        elif pilihan == '4':
            kembalikan_buku()
        elif pilihan == '5':
            lihat_data_peminjam()
        elif pilihan == '6':
            lihat_list_buku()
        elif pilihan == '7':
            break
        else:
            print('Menu tidak ada, silahkan pilih menu yang ada')


def cari_peminjam():
    keyword = input("Masukkan nama peminjam yang ingin Anda cari: ")

    if keyword == '':
        print('Input tidak boleh kosong!')
        return

    with open(file_txt, 'r') as file:
        hasil = []
        for peminjam in file:
            peminjam = eval(peminjam)
            if keyword in peminjam['peminjam']:
                hasil.append(peminjam)

    if hasil:
        print(f"Peminjam dengan nama '{keyword}' ditemukan:")
        for peminjam in hasil:
            print(f"Nama peminjam: {peminjam['peminjam']}")
            print(f"Judul buku: {peminjam['judul']}")
            print(f"Tanggal peminjaman: {peminjam['tanggal']}")
            print(f"Status peminjaman: {peminjam['status']}")
            print()
    else:
        print(f"Tidak ada peminjam dengan nama '{keyword}' yang ditemukan.")


def cari_buku(daftar_buku):
    keyword = input("Masukkan kata kunci yang ingin Anda cari: ")

    if keyword == '':
        print('Input tidak boleh kosong!')
        return

    hasil_pencarian = []
    for buku in daftar_buku:
        if keyword in buku['judul'] or keyword in buku['penerbit'] or keyword in str(buku['tahun']):
            hasil_pencarian.append(buku)
    if len(hasil_pencarian) > 0:
        print("Berikut adalah hasil pencarian untuk kata kunci '{}':".format(keyword))
        for buku in hasil_pencarian:
            print(
                "- {} ({}), diterbitkan oleh {}".format(buku['judul'], buku['tahun'], buku['penerbit']))
    else:
        print("Tidak ditemukan buku yang sesuai dengan kata kunci '{}'".format(keyword))


def pinjam_buku():
    nama_peminjam = input('Input nama peminjam: ')
    judul_buku = input('Input judul buku: ')
    tanggal_pinjam = input('Input tanggal pinjam (dd/mm/yyyy): ')

    if nama_peminjam == '' or judul_buku == '' or tanggal_pinjam == '':
        print('Input tidak boleh kosong!')
        return

    # Perulangan
    for buku in daftar_buku:
        if buku['judul'] == judul_buku:
            # Operasi File
            with open(file_txt, 'a') as file:
                # Dictionary
                data = {
                    'peminjam': nama_peminjam,
                    'judul': judul_buku,
                    'status': 'pinjam',
                    'tanggal': tanggal_pinjam
                }
                file.write(str(data) + '\n')
                print('Peminjaman Berhasil!')
                break
    else:
        print('Buku tidak ada')


def kembalikan_buku():
    nama_peminjam = input('Input nama peminjam: ')
    tanggal_pinjam = input('Input tanggal pinjam (dd/mm/yyyy): ')

    if nama_peminjam == '' or tanggal_pinjam == '':
        print('Input tidak boleh kosong!')
        return

    # Operasi File
    with open(file_txt, 'r+') as file:
        isi = file.readlines()
        for i, baris in enumerate(isi):
            data = eval(baris)
            if data['peminjam'] == nama_peminjam and data['tanggal'] == tanggal_pinjam:
                for buku in daftar_buku:
                    if buku['judul'] == data['judul']:
                        data['status'] = 'selesai'

                        isi[i] = str(data) + '\n'
                        file.seek(0)
                        file.writelines(isi)
                        print('Pengembalian Berhasil!')
                        break
                break
        else:
            print('Data tidak ada')


def lihat_data_peminjam():
    # Operasi File
    with open(file_txt, 'r') as file:
        print()
        for isi in file:
            # Dictionary
            data = eval(isi)
            print('Peminjam: {} \t Judul: {} \t Status: {} \t Tanggal: {}'.format(
                data['peminjam'], data['judul'], data['status'], data['tanggal']))
            print()


def lihat_list_buku():
    # Perulangan
    for buku in daftar_buku:
        print(
            "- {} ({}), diterbitkan oleh {}".format(buku['judul'], buku['tahun'], buku['penerbit']))


main()
