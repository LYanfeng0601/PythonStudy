'''
alien = {"color":"green","point":"5"}
# 访问字典中的值
p=alien['point']
print("you kill a\t" +alien['color']+"\talien:and you get\t"+str(p))
#t添加键值对
alien['heigh']='100'
alien['weight']='80'
print(alien)
'''
#x修改字典中的值
alien={'x':0,'y':0,'speed':'fast'}
if alien['speed'] == 'slow':
    alien['x']=1
elif alien['speed']=='mediu':
    alien['x']=2
elif alien['speed']=='fast':
    alien['x']=3
print(alien)
# 删除键值
del alien['y']
print(alien)
# 遍历字典中所有的键与值
for key,value in alien.items():
    print("\nkey  "+ key)
    print("\nvalue  "+ str(value))

# 遍历字典中所有的键
for keys in alien.keys():
    print("\nkey  "+ keys)

