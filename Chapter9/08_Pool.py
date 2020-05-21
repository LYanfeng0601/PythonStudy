#coding=utf-8
import time,os,random
import multiprocessing
###任务数不确定，用进程池
def test2(tmp):
    print(tmp)
    print(os.getpid())
    time.sleep(2)
    print("**********************************")
def main():
    po = multiprocessing.Pool(4) #创建进程池
    for i in range(0,10):
        po.apply_async(test2,(i,)) #添加任务到进程池
        #print("****************start****************")
    po.close() #关闭进程池
    po.join()  #等待po中的子进程执行完成，必须在close之后
    print("###############end###################")
if __name__ == "__main__":
    main()