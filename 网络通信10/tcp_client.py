#coding=utf=8
import socket

def main():
	tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	tcp_socket.connect(("192.168.0.102",8080))
	tcp_socket.send(input("please input").encode("utf-8"))	
	tcp_socket.close()
if __name__ == "__main__":
	main()
