#创建列表
names=['liyanfneg','nanyixian','lisi','wangliu']
#访问列表元素
print(names)#将列表打印出来，包括格式
#通过列表下标访问
print(names[0])
print(names[-1])
print(names[1:3])#从下表为1到下标为3的前一个
#添加元素
names.append("tinajia")#添加至列表的最后
print(names[-1])
names.insert(0,"tianjia0")#添加至指定位置
print(names)
#列表中元素的修改
print(" 修改前列表第一个元素的值为"+names[0])
names[0]="xiugai"
print(" 修改后列表第一个元素的值为"+names[0])
#从列表中删除元素
print(names)
del names[0]#指定列表元素的下标进行删除  永久删除
print(names)
names.remove("lisi")#根据元素值进行删除
print (names)
name_pop=names.pop(0)#弹出指定的值，但任然可以访问
print(name_pop)
print(names)


