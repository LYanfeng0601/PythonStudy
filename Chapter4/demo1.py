#for循环遍历所有的元素
'''
names=['lisi','wangwu','maliu','zhangsan ']
for name in names:
    print ("hello"+"  "+name.title()+"\n")
for num in range(1,5):#生成1-4的=数
    print(num)
a=range(3,8)
print(list(a))#将生成的数转变为列表
for i in range(2,10,2):
    print(i)
# 计算1-10 的平方  并储存在列表中
suquals=[]
for suqual in range(1,11):
    suquals.append(suqual**2)
print(suquals)
digits=[1,3,2,7,22,66,33,22,434,5,3,]
print(min(digits))
print(max(digits))
print(sum(digits))
#列表的解析
sq=[value**2 for value in range(1,11)]
print(sq)
'''
#切片
players=['charles','martin','michael','florence','eli']
print(players[0:3])#打印1到3个
print(players[:4])#打印前四个
print(players[-3:])#打印倒数三个
#遍历切片
print("*********************************")
for i in players[-3:]:
    print(i)
#复制列表
'''  #错误的复制
my_food=['pizza','falafel','carrot']
friend_food=my_food
print(my_food)
my_food.append('sd')
friend_food.append('aa')
print(my_food)
print(friend_food)
'''
my_food=['pizza','falafel','carrot']
friend_food=my_food[:]
print(my_food)
my_food.append('sd')
friend_food.append('aa')
print(my_food)
print(friend_food)
# 元组：用（）括号，值不能修改，但可以重新定义
dims=(100,22)
print(dims)
#dims[0]=1  错误写法
print(dims)
dims=(222,22)#可以重新定义
print(dims)
for i in dims:
    print(i)
