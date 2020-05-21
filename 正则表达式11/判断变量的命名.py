#coding=utf-8
import re
def main():
	names = ["test1","_test2","test$","123tede_","23test"]
	for name in names:
		ret = re.match(r"^[a-zA-Z_]+[a-zA-Z_0-9]*$",name)
		if ret:
			print("变量名:%s 符合要求" %name)
		else:
			print("变量名:%s  不符合要求" %name)


if __name__ == "__main__":
	main()
