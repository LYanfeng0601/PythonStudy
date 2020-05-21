#coding=utf-8
import multiprocessing
import time

def download(q):
    data = [11,22,33,44]
    for tmp in data:
        q.put(tmp)#写入数据
    print("&&&&&&&&&&&&dowmload&&&&&&&&&&&&&&&&")
def get_data(q):
    wating_list = list()
    while True:
        date = q.get()#获得数据
        wating_list.append(date)
        if q.empty():
            break
    print(wating_list)

def main():
    #1. 创建一个队列
    q = multiprocessing.Queue()
    #2，创建多个进程，将队列的引用作用实参传传递到里面
    p1 = multiprocessing.Process(target=download,args=(q,))
    p2 = multiprocessing.Process(target=get_data,args=(q,))
    p1.start()
    p2.start()
if __name__=="__main__":
    main()