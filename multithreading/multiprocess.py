from multiprocessing import Process
import time
def f(n):
    time.sleep(1)
    return n**n

def main0():
    s_time = time.time()
    all_pro = {}
    for i in range(9):
        p = Process(target=f,args=[i,])
        all_pro[i] = p
        p.start()
    for i in range(9):
        all_pro[i].join()
    e_time = time.time()
    print("main0:%d"%(e_time-s_time))

def main1():
    s_time = time.time()
    for i in range(9):
        f(i)
    e_time = time.time()
    print("main1:%d"%(e_time-s_time))

if __name__ == '__main__':
    main0()
    main1()