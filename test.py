# Program Peminjaman Buku Perpustakaan

# List Dictionary
daftar_buku = [
    {
        'judul': 'asd',
        'jumlah': 0
    },
    {
        'judul': 'qwe',
        'jumlah': 10
    },
]

file_txt = 'buku.txt'


def main():
    while True:
        # Menampilkan Menu
        print('Menu Peminjaman Buku Perpustakaan:')
        print('1. Pinjam Buku')
        print('2. Kembalikan Buku')
        print('3. Lihat Data Peminjam')
        print('4. Lihat List Buku')
        print('5. Keluar Menu')

        pilihan = input('Pilih menu: ')

        # Percabangan
        if pilihan == '1':
            pinjam_buku()
        elif pilihan == '2':
            kembalikan_buku()
        elif pilihan == '3':
            lihat_data_peminjam()
        elif pilihan == '4':
            lihat_list_buku()
        elif pilihan == '5':
            break
        else:
            print('Menu tidak ada, silahkan pilih menu yang ada')


def pinjam_buku():
    nama_peminjam = input('Input nama peminjam: ')
    judul_buku = input('Input judul buku: ')
    jumlah_buku = int(input('Input jumlah buku: '))
    tanggal_pinjam = input('Input tanggal pinjam (dd/mm/yyyy): ')
    # Perulangan
    for buku in daftar_buku:
        if buku['judul'] == judul_buku:
            if buku['jumlah'] >= jumlah_buku:
                buku['jumlah'] -= jumlah_buku
                # Operasi File
                with open(file_txt, 'a') as file:
                    # Dictionary
                    data = {
                        'peminjam': nama_peminjam,
                        'judul': judul_buku,
                        'jumlah': jumlah_buku,
                        'status': 'pinjam',
                        'tanggal': tanggal_pinjam
                    }
                    file.write(str(data) + '\n')
                    print('Peminjaman Berhasil!')
                    break
            else:
                print('Jumlah buku tidak cukup')
                break
    else:
        print('Buku tidak ada')


def kembalikan_buku():
    nama_peminjam = input('Input nama peminjam: ')
    tanggal_pinjam = input('Input tanggal pinjam (dd/mm/yyyy): ')
    # Operasi File
    with open(file_txt, 'r+') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            # Dictionary
            data = eval(line)
            if data['peminjam'] == nama_peminjam and data['tanggal'] == tanggal_pinjam:
                for buku in daftar_buku:
                    if buku['judul'] == data['judul']:
                        buku['jumlah'] += data['jumlah']
                        data['status'] = 'selesai'

                        lines[i] = str(data) + '\n'
                        file.seek(0)
                        file.writelines(lines)
                        print('Pengembalian Berhasil!')
                        break
                break
        else:
            print('Data tidak ada')


def lihat_data_peminjam():
    # Operasi File
    with open(file_txt, 'r') as file:
        print()
        print('Nama\tJudul\tJumlah\tStatus\tTanggal')
        for line in file:
            # Dictionary
            data = eval(line)
            print(data['peminjam'], '\t', data['judul'], '\t',
                  data['jumlah'], '\t', data['status'], '\t', data['tanggal'])
            print()


def lihat_list_buku():
    # Perulangan
    for buku in daftar_buku:
        if buku['jumlah'] > 0:
            print(buku['judul'], '\t', buku['jumlah'])
        else:
            print(buku['judul'], '\t', 'Habis')


main()
