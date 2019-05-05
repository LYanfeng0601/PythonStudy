#coding=utf-8
import socket

def deal_with(sock_request,addr_request):
	while True:
		recv_data = sock_request.recv(1204)
		#send_data = input("please input your words")
		send_data = "<h1>hello world</h1>"
		if recv_data:
			print(recv_data.decode("utf-8"))
			sock_request.send(send_data.encode("utf-8"))
		else:
			break

def main():
	tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	tcp_socket.bind(("192.168.0.106",7788))
	tcp_socket.listen(128)
	while True:
		new_sock,new_addr = tcp_socket.accept()
		print(new_sock)
		deal_with(new_sock,new_addr)
		new_sock.close()
	tcp_socket.close()
if __name__ == "__main__":
	main()
