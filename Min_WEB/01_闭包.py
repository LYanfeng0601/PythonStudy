# 闭包
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
