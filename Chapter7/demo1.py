"""
message=input("please input somethings")
print(message)
promt="please tell me where you from"
promt+="\nwhat is your name "
print(input(promt))
"""
'''
age=input("please input your age ")
if int(age) >20:
    print("成年人")
else:
    print("未成年人")
              '''
""" while语句"""
'''
active = True
while active:
    message=input("请输入您要表达的话")
    if message == "quit":
        active=False
    print("message")
   '''
'''
while True:
    m=input("请输入您去过的地方")
    if m == 'quit':
        break
    else:
        print("i wolod like to "+m)
   '''

'''continue的用法'''
a=1
while a < 20:
   a += 1
   if a%2 == 0:
       continue
   print(a)


