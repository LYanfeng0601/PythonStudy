#coding=utf-8
import socket
import sys

def deal_with(new_sock,file_name):
	try:	
		
		f = open(file_name,"rb")
		file_content = f.read()
		print(file_content)
		new_sock.send(file_content)
	except Exception as ret:
		f.close()

def main():
	server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server_socket.bind(("192.168.0.103",7788))
	server_socket.listen(128)
	new_sock,new_addr = server_socket.accept()
	file_name = new_sock.recv(1024)
	print(file_name.encode("utf-8"))
	print(new_sock)
	print(new_addr)
	deal_with(new_sock,file_name)
	#new_sock.close()
	#server_socket.close() 
	
		

if __name__ == "__main__":
	main()
