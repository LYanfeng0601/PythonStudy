# 闭包: 嵌套的内部函数可以用外部的函数的变量
## 函数
def line_6(k, b):
    def create_y(x):
        print(k * x + b)
    return create_y

line_6_1 = line_6(1, 2)
line_6_1(0)
line_6_1(1)
line_6_1(2)
line_6_1 = line_6(11, 122)
line_6_1(0)
line_6_1(1)
line_6_1(2)
print("*"*20)