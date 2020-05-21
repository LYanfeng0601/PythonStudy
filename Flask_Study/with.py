# coding:utf-8
class Foo(object):
    def __enter__(self):
        print("enter called")
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("离开方法")

    # 上下文管理器
with Foo() as foo:
    print("hello python")