#coding="UTF-8"
import time

def login():
	return "welcome to login %s" % time.ctime()

def register():
	return "welcome to register %s" % time.ctime()

def erro_log():
	return "your request is erro"

def application(file_name):
	if file_name == "/login.py":
		return login()
	elif file_name == "/register.py":
		return register()
	else:
		return erro_log()
		
	
