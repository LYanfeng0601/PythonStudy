import socket

def main():
	#  1. 创建套接字
	tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	#  2. 绑定端口
	tcp_socket.bind(("192.168.0.106",7788))
	
	#  3. 设置为监听模式
	tcp_socket.listen(127)

	#  4. 等待用户的链接
	while True:
		new_socket,new_addr = tcp_socket.accept()
		print(new_socket)
		print(new_addr)	
		
		#  5. 接受发送数据
		while True:
			recv_data = new_socket.recv(1024)
			print(recv_data)
			if recv_data:

				print("客户：%s" % recv_data.decode("utf-8"))
				send_data = input("to client")
				new_socket.send(send_data.encode("utf-8"))
			else:
				break
		new_socket.close()
		
	#  6. 关闭套接字
	tcp_socket.close()
	

if __name__ == "__main__":
	main()
