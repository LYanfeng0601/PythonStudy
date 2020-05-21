#coding=utf-8
import re

def main():
	email = input("请输入邮箱")
	print ("您输入的邮箱是：%s" %email)
	rec = re.match(r"[a-z0-9A-Z]{1,20}@163\.com$",email)  #此处 需要反斜杠进行转义
	#print (rec.group())
	if rec:
		print ("您输入的邮箱是：%s*********符合规则" %email)
	else:
		print ("您输入的邮箱是：%s,**********不符合规则" %email)
if __name__ == "__main__":
	main()
