#coding=utf-8
import socket
import re
import threading
import select

def deal_with(sock_request,send_data):

	request_data = sock_request.recv(1024).decode("utf-8")
	if request_data:
		requests_lines = request_data.splitlines()
		ret = re.match(r"[^/]+(/[^ ]*)",requests_lines[0])
		file_name = ""
		if ret:
			file_name = ret.group(1)
			print("*"*40,file_name)
		try:
			if file_name == "/":
				file_name = "/index.html"
				print("*"*40,file_name)
			if ".html" in file_name:
				file_path = "./html"
				f = open(file_path+file_name,"rb")
			else:
				file_path = file_name
				f = open(file_name,"rb")
		except:
			send_data = "HTTP/1.1 404 not found\r\n"
			send_data += "\r\n"
			send_data += "*************file not found*****************"
			sock_request.send(send_data.encode("utf-8"))
		else:
			index_content = f.read()
			send_data = "HTTP/1.1 200 OK\r\n"
			send_data += "\r\n"
			sock_request.send(send_data.encode("utf-8"))
			sock_request.send(index_content)
			f.close()
	sock_request.close()

def main():
	tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	tcp_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)  # 设置端口可重复利用
	tcp_socket.bind(("192.168.0.106",7788))
	tcp_socket.listen(128)
	epl = select.epoll()  # 创建epoll对象
 	epl.register(tcp_socket.fileno(),select.EPOLLIN())
	fd_event_dict = dict{}
	while True:
		fd_envet = epl.poll()  #  默认堵塞，知道os检测到数据到来，通过事件通知方式告诉程序，此时才会解堵塞,返回列表
		## fd_envet [(fd,event())]
		for fd,envent in fd_envet:
			if fd == tcp_socket.fileno():
				new_sock,new_addr = tcp_socket.accept()
				epl.register(new_sock.fileno(),select.EPOLLIN)
				fd_event_dict[new_sock.fileno()] = new_sock
			elif event == select.EPOLLIN:
				## p判断已经链接的客户端是否有数据发过来
				recv_data = fd_event_dict[fd].recv(1024).decode("utf-8")
			if recv_data:
				deal_with(fd_event_dict[fd],recv_data)
			else:
				fd_event_dict[fd].close()
				epl.unregister(fd)
				del fd_event_dict[fd]
	tcp_socket.close()
if __name__ == "__main__":
	main()
