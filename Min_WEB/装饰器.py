
import time


def login_check(funs):
    def check_result():
        print("**********start check logining***********")
        start_time = time.time()
        funs()
        end_time = time.time()
        print("all time is %f" % (end_time - start_time))
    return check_result


# 无返回值，无参数
@login_check  # 此处相当于login = login_check(login)
def login():
    print("############I am ready logining###############")

    for i in range(10):
        print(i)
login()


# 有参数

def check_register(fun):
    def excute_check(num):
        print("start check function")
        fun(num)
    return excute_check


@check_register
def register(id):
    print("my id is  % d " % id)
register(100)
