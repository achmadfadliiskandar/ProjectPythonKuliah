import threading

# def tugas1():
#     print("tugas 1 Selesai")

def print_cube(num):
    print("Cube : {}".format(num * num * num))

# def tugas2():
#     print("tugas 2 selesai")

def print_square(num):
    print("Square : {}".format(num * num))

# menmapilkan tugas trhreadnya

# data1 = threading.Thread(target=tugas1)
# data2 = threading.Thread(target=tugas2)

if __name__ == "__main__":
    data1 = threading.Thread(target=print_cube,args=(10,))
    data2 = threading.Thread(target=print_square,args=(10,))

# menjalankan treadingnya
data1.start()
data2.start()

# menggabungkan trhreadnya
data1.join()
data2.join()

print("done")