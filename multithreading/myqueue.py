from multiprocessing import Process,Queue
import time
def write(q):
    for i in ['a','b','c','d']:
        print('put %s' % i)
        q.put(i)
        time.sleep(1)

def read(q):
    while True:
        x = q.get(True)
        print('get %s' % x)

def main():
    q = Queue(10)
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    pw.start()
    pr.start()
    pr.join()

if __name__ == '__main__':
    main()