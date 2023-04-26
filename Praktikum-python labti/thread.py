import threading
from threading import Thread
import time

# import threading
# import time

# kasus olah 1000000 data
class OlahData:
    def __init__(self,rentang):
        self.rentang = rentang
    def readData(self):
        print('[1] Read data Ke : {}'.format(self.rentang))
        time.sleep(2)
    def sortData(self):
        print('[1] Sort data Ke : {}'.format(self.rentang))
        time.sleep(1)
    def exportData(self):
        print('[1] Export data Ke : {}'.format(self.rentang))
        time.sleep(1)
    def run(self):
        self.readData()
        self.sortData()
        self.exportData()

if __name__ == '__main__':
    start = time.perf_counter()
    rentangs = [
        '1-100000',
        '10001-200000',
        '20001-300000',
        '30001-400000',
        '40001-500000',
        '50001-600000',
        '60001-700000',
        '70001-800000',
        '80001-900000',
        '90001-100000',
    ]
    # for rentang in rentangs:
    #     OlahData(rentang).run()
    #     finish = time.perf_counter()
    #     print('Waktu Total : ',finish-start)

    thread_list = []
    for rentang in rentangs:
        t = Thread(target=OlahData(rentang).run)
        t.start()
        time.sleep(0.1)
        thread_list.append(t)
    for thread in thread_list:
        thread.join()
        finish = time.perf_counter()
        print('Waktu Total : ',finish-start)