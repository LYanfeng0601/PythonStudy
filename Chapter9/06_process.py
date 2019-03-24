#coding=utf-8
import time
import multiprocessing

def test1():
   # time.sleep(1)
    #for i in range(100):
     #   print("test1")
    #time.sleep(1)
    while True:
        print ("+++++++test1++++++++")

def test2():
    #for i in range(100):
        #print("test2")
    while True:
        print("*********test2***********")
    #time.sleep(1)
def main():
    p1 = multiprocessing.Process(target=test1)
    p2 = multiprocessing.Process(target=test2)
    po = multiprocessing.Pool(1)
    p1.start()
    time.sleep(2)
    p2.start()
if __name__ == "__main__":
    main()