from multiprocessing import Pool
import time

def f(x):
    time.sleep(2)
    return x**x

def main0():
    s_time = time.time()
    pool = Pool(processes=5)
    for i in range(10):
        res = pool.apply_async(f,(i,))  #异步
    pool.close() #关闭pool，使其不在接受新的任务。
    pool.join()
    e_time = time.time()
    print("main0:%s" % (e_time - s_time))

def main1():
    s_time = time.time()
    pool = Pool(processes=5)
    for i in range(10):
        res = pool.apply(f,(i,))    #同步
    pool.close() #关闭pool，使其不在接受新的任务。
    pool.join()
    e_time = time.time()
    print("main1:%s" % (e_time - s_time))

if __name__ == '__main__':
    main0()
    #main1()