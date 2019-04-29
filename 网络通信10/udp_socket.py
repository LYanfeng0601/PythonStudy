#coding=utf-8
import socket

def main():
	while True:
		send_data = input("请输入发送的内容")
		#if send_data == "exit":
		#	break
		udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)   # 创建套接字
		local_port = ('',7788)  ## ip 为空，表示本机的ip，一般省略
		udp_socket.bind(local_port)   ## 绑定端口 必须绑定自己的IP以及端口
		#udp_socket.sendto(b"hahahahah_______,("192.168.0.102",8085))  # IP跟端口应该放到一个远足中
		udp_socket.sendto(send_data.encode("utf-8"),("192.168.0.102",8080))  # IP跟端口应该放到一个远足中
		##接受数据
		#re_data = udp_socket.recvfrom(1024)  # 1024表示接受的大小,是个元组
		#print(re_data)
		#re_mes = re_data[1]  # 存储接收到的 IP  port
		#re_add =re_data[0]  # 存储接收到的数据
		#print("%s:%s" % (str(re_mes),re_add.decode("gbk")))  # windows 上的默认数据类型是gbk
		####解析接收到的数据
		udp_socket.close()  ## 关闭字节套

if __name__ == "__main__":
	main()
