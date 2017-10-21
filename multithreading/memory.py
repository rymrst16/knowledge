from multiprocessing import Process
import threading
import time

lock = threading.Lock()

def run(info_list,n):
    lock.acquire()
    info_list.append(n)
    time.sleep(1)
    lock.release()
    print('%s\n' % (info_list,))


def main0():   #多进程
    info_list = []
    all_pro = []
    for i in range(10):
        t = Process(target=run,args=[info_list,i])
        all_pro.append(t)
        t.start()
    for t in all_pro:
        t.join()

def main1():   #多线程
    info_list = []
    all_the = []
    for i in range(10):
        t = threading.Thread(target=run,args=[info_list,i])
        all_the.append(t)
        t.start()
    for t in all_the:
        t.join()

if __name__ == '__main__':
    print("多进程####################################")
    main0()
    print("多线程####################################")
    main1()