def fungsi():
    print("KONVERSI NILAI MATEMATIKA")
    uts = int(input("Masukan Nilai UTS : "))
    uas = int(input("Masukan Nilai UAS : "))
    quiz = int(input("Masukan Nilai QUIZ : "))
    rata_rata = uas + uts + quiz
    save_nilai = rata_rata / 3 # INI ADALAH NILAI RATA
    print(save_nilai)

    # nah sekarang hitungan untuk rata-rata dan predikatnya
    if save_nilai > 80 :
        print("GRADE ANDA ADALAH :  A\nPREDIKAT ANDA : SANGAT MEMUASKAN")
        konfirmasi = input("MAU LAGI NGGAK BOS ?? : ")
        if konfirmasi != "tidak":
            fungsi()
        else:
            exit()
    elif save_nilai > 70:
        print("GRADE ANDA ADALAH :  B\nPREDIKAT ANDA : MEMUASKAN / BAIK")
        konfirmasi = input("MAU LAGI NGGAK BOS ?? : ")
        if konfirmasi != "tidak":
            fungsi()
        else:
            exit()
    elif save_nilai > 55:
        print("GRADE ANDA ADALAH :  C\nPREDIKAT ANDA : CUKUP")
        konfirmasi = input("MAU LAGI NGGAK BOS ?? : ")
        if konfirmasi != "tidak":
            fungsi()
        else:
            exit()
    elif save_nilai > 40:
        print("GRADE ANDA ADALAH :  D\nPREDIKAT ANDA : KURANG")
        konfirmasi = input("MAU LAGI NGGAK BOS ?? : ")
        if konfirmasi != "tidak":
            fungsi()
        else:
            exit()
    else:
        print("GRADE ANDA ADALAH :  E\nPREDIKAT ANDA : KURANG BANGET")
        konfirmasi = input("MAU LAGI NGGAK BOS ?? : ")
        if konfirmasi != "tidak":
            fungsi()
        else:
            exit()
fungsi()