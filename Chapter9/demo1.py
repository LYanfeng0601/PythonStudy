import time
import threading
def sing():
    for i in range(5):
        print("sing********************")
        time.sleep(1)
def dance():
    for i in range(5):
        print("dance+++++++++++++++++++")
        time.sleep(1)
def main():
    # 创建子线程对象
    t1 = threading.Thread(target=sing) #函数名（）；调用函数     函数名；指定函数的位置
    t2 = threading.Thread(target=dance)
    t1.start()
    time.sleep(1)
    t2.start()
    time.sleep(1)
  #  while True:
   #     for tmp in threading.enumerate():  #线程数
     #       if threading.enumerate() < 0:
      #          print ("over")
      #          break
       #     else:
    print (threading.enumerate())
if __name__ == "__main__":
    main()

