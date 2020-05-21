#coding=utf-8
import time
import threading

def test1(tmp):
    global num  #当对变量有改动（指向变了的时候，应加global）
    num += 1
    print (num)

    print (str(tmp))

def test2():
    print(num)

if __name__ =="__main__":
    num = 1
    test = [111,2200]
    ## target 指定函数去哪儿，args指定传的参数
    t1 = threading.Thread(target=test1,args=(test,))  ## 注意 此处只能传元组
    t2 = threading.Thread(target=test2)
    t1.start()
    time.sleep(1)
    t2.start()