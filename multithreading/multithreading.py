from threading import Thread
import time
def my_thread():
    i = 0
    for _ in range(500000000):
        i += 1
    return True

def main0():
    s_time = time.time()
    for i in range(2):
        t = Thread(target=my_thread)
        t.start()
        t.join()
    e_time = time.time()
    print("main0:%d"%(e_time-s_time))

def main1():
    s_time = time.time()
    all_thread = {}
    for i in range(2):
        t = Thread(target=my_thread)
        all_thread[i] = t
        t.start()
    for i in range(2):
        all_thread[i].join()
    e_time = time.time()
    print("main1:%d"%(e_time-s_time))

if __name__ == '__main__':
    main0()
    main1()