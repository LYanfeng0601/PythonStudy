#4-1
pizaas=['sanmingzhi','dangao','caijiabing']
for pizaa in pizaas:
    print (pizaa)
    print("i kile "+pizaa+"pizza"+"\n")
print("i really like it")
#4-2
animals=['dod','cat','pig']
for animal in animals:
    print (animal)
    print("a "+animal+"is a kind pet")
print("they all have hair")
#4-3 使用一个for循环打印1-20
for i in range(1,21):
    print(i)
#4-4创建一个数字列表 内容为1-100
nums=[]
for num in range(1,1000001):
    nums.append(num)
print(max(nums))
print(min(nums))
print(sum(nums))
#4-6 创建1-20中的奇数
for j in range(1,21,2):
    print(j)
#4-7 创建一个列表，其中包含3-30内能被3整除的数字，并将它们打印出来放在列中
ks=[k for k in range(3,30,3)]
print(ks)
#4-8
ls=[l**3 for l in range(1,11)]
print(ls)
#4-9
#4-10
#4-11
#4-13