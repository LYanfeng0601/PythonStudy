def set_func(func):
    print("开始装饰")

##通用装饰器
    def call_fun(*args,**kargs):
        print("权限验证一")
        print("权限验证一")
        return func(*args,**kargs)
    return call_fun

@set_func
def login(num,*args,**kargs):
    print("***************test1******************%d" % num)
    print("***************test******************",args)
    print("***************test1******************",kargs)
    return "OK"

ret = login(100,200)
print(ret)