#coding=utf-8
import time
from collections import Iterable
from collections import Iterator
class Classmate(object):
    def __init__(self):
        self.names = list()

    def add_name(self, name):
        self.name = name
        self.names.append(name)

    def __iter__(self):  # 一个类中有该方法，说明该类可以迭代
        return Iter_mate(self)


class Iter_mate(object):
    def __init__(self, obj):
        self.obj = obj
        self.current_num = 0
    def __iter__(self):
        pass

    def __next__(self):
        res = self.obj.names[self.current_num]
        return self.obj.names[self.current_num]
        self.current_num +=1
        return ret


if __name__ == "__main__":
    classmate = Classmate()
    classmate.add_name("zhangsan")
    classmate.add_name("lisi")
    classmate.add_name("wangwu")
    # class_iterator = Iter_mate(classmate)
    #for tmp in classmate:
       # print(tmp)
       # time.sleep(1)
        #print ("is or not Iterable :",isinstance(classmate,Iterable)) #判断是否可迭代
        #print ("is or not a Iterator",isinstance(class_iterator,Iter_mate)) #判断是否为迭代器
