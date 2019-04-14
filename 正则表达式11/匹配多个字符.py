#coding=utf-8

import re


#{1,3} 表示前面的可以示1-3个
rec = re.match(r"hello\d{1,3}","hello1qq")
print (rec.group())

#{8}  表示前面的必须为多少位
rec = re.match(r"\d{11}","15686270601")
print (rec.group())

# ? 前面的东西可有可无

rec = re.match(r"\d{3}-?\d{7}","026-1111111")
print (rec.group())

# * 表示前面的可有多个或没有  除了\n
html = """aaa
ddd
cccc"""
print (html)
rec = re.match(r".*",html)
print (rec.group())
rec= re.match(r".*",html,re.S)
print (rec.group())

# + 至少一次
rec= re.match(r"1+","1")
print (rec.group())
