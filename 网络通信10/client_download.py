#conding=utf-8
import socket
import sys
def main():
	client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	client_socket.connect(("192.168.0.103",7788))
	file_name = input("请输入下载的文件名")
	client_socket.send(file_name.encode("utf-8"))
	recv_data = client_socket.recv(1024)
	print(recv_data.decode("utf-8"))
	if recv_data:
		with open("copy_" + file_name,"wb") as f:
			f.write(recv_data)
	client_socket.close()
if __name__ == "__main__":
	main()
