# coding=utf-8
import time
import threading
g_num = 0
def test1(num):
    global g_num
    mecx.acquire()
    for i in range(num):
         g_num += 1
    mecx.release()
    print("test1++++++++++%d",g_num)
def test2(num):
    global g_num
    mecx.acquire()#上锁：如果之前没上锁，上锁成功；如果之前已上锁，则会阻塞在这儿
    for i in range(num):
        g_num += 1
    mecx.release()
    print ("test2+++++++++++++%d",g_num)
mecx = threading.Lock()
def main():
    t1 = threading.Thread(target=test1,args=(10000000,))
    t2 = threading.Thread(target=test2,args=(10000000,))
    t1.start()
    #time.sleep(1)
    t2.start()

if __name__ == "__main__":
    main()
