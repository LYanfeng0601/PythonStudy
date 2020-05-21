#coding = utf-8
import re
# 单个字符的匹配

rec = re.match(r"hello","hello world")
print (rec.group())

# \d  表示单个数字
rec = re.match(r"hello\d","hello1")
print (rec.group())

#[1-8]表示1-8之前的一个数字

rec = re.match(r"hello[1-8]","hello1")
print (rec.group())

#[]中也可以是字母

rec = re.match(r"hello[1-8a-zA-Z]","helloa")
print (rec.group())

# "\w" 等价于a-z\0-9\A-Z\_  注意；还包括中文等，慎用
rec = re.match(r"hello\w","hello_")
print (rec.group())

# "\s" 表示空格或者tab
rec = re.match(r"hello\s[1-3]","hello 1")
print (rec.group())

# "\D"   表示不是数字
# “\S”   表示非空

# “.”  表示一个字符
rec = re.match(r"hello.","hello&")
print (rec.group())


















