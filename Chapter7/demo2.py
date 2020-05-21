unconfirm_users = ['zhangsan','lisi','wangwu']
confirm_users = []
while unconfirm_users:
    confiming_users = unconfirm_users.pop()
    print("now confirm user is "+confiming_users)
    confirm_users.append(confiming_users.title())
for c in confirm_users:
    print(c)
print(unconfirm_users)

''' 使用用户输入填充字典'''
responses={}
active=True
while active:
    name=input("your name ?")
    response=input("where are you from")
    responses[name]=response
    repet=input("next or no")
    if repet == 'no':
        active = False


