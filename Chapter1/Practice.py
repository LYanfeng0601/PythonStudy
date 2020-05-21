#3-4
lists=['liyanfeng','nanyixian','wangwu']
print(lists[0]+":先生您好,特邀您共进晚餐")
print(lists[1]+":先生您好,特邀您共进晚餐")
print(lists[2]+":先生您好,特邀您共进晚餐")
#3-5
print("非常遗憾，"+lists[2]+"先生有事不能参加我们的晚宴")
lists[2]="maliu"
print(lists[0]+":先生您好,特邀您共进晚餐")
print(lists[1]+":先生您好,特邀您共进晚餐")
print(lists[2]+":先生您好,特邀您共进晚餐")
#3-6
print("we are lucky,i find a bigeer table")
lists.insert(0,"heshen")
lists.insert(2,"jixiaonan")
lists.append("qianlong")
print(lists[0]+":先生您好,特邀您共进晚餐")
print(lists[1]+":先生您好,特邀您共进晚餐")
print(lists[2]+":先生您好,特邀您共进晚餐")
print(lists[3]+":先生您好,特邀您共进晚餐")
print(lists[4]+":先生您好,特邀您共进晚餐")
print(lists[5]+":先生您好,特邀您共进晚餐")

print("总人数为"+str(len(lists)))
#3-7
print("we are sorry, we only can invite two people to dinner")
lis1=lists.pop()
print(lis1+"先生，不好意思，您没法参加我们的晚宴。")
lis2=lists.pop()
print(lis2+"先生，不好意思，您没法参加我们的晚宴。")
lis3=lists.pop()
print(lis3+"先生，不好意思，您没法参加我们的晚宴。")
lis4=lists.pop()
print(lis4+"先生，不好意思，您没法参加我们的晚宴。")
print(lists[0]+"  "+lists[1]+"恭喜您两位可以继续参加我们的晚宴")
print(lists)
del lists[0]
del lists[0]
print(lists)
print("------------------------------------------------")
#3-8
travls=['beijing','shanghai','guangdong','shenzhou','lanzhou']
print (travls)
print(sorted(travls))
print(travls)
print(sorted(travls,reverse=True))
print(travls)
travls.reverse()
print (travls)
travls.reverse()
print (travls)
travls.sort()
print(travls)
travls.sort(reverse=True)
print (travls)