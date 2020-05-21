def greet(username):
    print("nihao\t"+username)
greet('json')
#传递实参:顺序传递，关键字传递，默认值，也可以混搭
def cal(a,b=2,c=2):
    print("a是"+str(a))
    print("b是"+str(b))
    print("c是"+str(c))
#cal(a=1,c=4,b=3)
#cal(1,2,3)
def add(a='',b=''):
    return int(a)+int(b)