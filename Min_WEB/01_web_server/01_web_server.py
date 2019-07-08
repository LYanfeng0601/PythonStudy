#coding-"UTF-8"
import mini_frame_01
import time
import re
import socket
import multiprocessing
import sys

class WSGIServer(object):
	def __init__(self,port):
		self.tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
		self.tcp_server_socket.bind(('192.168.0.106',port))
		self.tcp_server_socket.listen(128)

	def server_client(self,new_socket):
		print(new_socket)
		request = new_socket.recv(1024).decode("utf-8")	
		request_lines = request.splitlines()
		file_name = ""
		ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
		if ret:
			html_content = ''
			file_name = ret.group(1)
			if file_name == "/":
				file_name = "/index.html"
			if not file_name.endswith(".py"):
				
				try:
					f = open("./html" + file_name, "rb")
				except:
					response = "HTTP/1.1 404 NOT FOUND\r\n"
					response += "\r\n"
					response += "------file not found-----"
					new_socket.send(response.encode("utf-8"))
				else:
					html_content = f.read()
					f.close()
					response = "HTTP/1.1 200 OK\r\n"
					response += "\r\n"
					new_socket.send(response.encode("utf-8"))
					new_socket.send(html_content)
			else:
				# 如果是以.py结尾，认为是动态请求
				env = dict()
				env['PATH_INFO'] = file_name
				body = mini_frame_01.application(env,self.set_response_header)
				header = "HTTP/1.1 %s\r\n" % self.status
				for tmp in self.headers:
					header += "%s:%s\r\n" % (tmp[0],tmp[1])
				header += "\r\n"	
				response = header + body
				new_socket.send(response.encode("utf-8"))
			new_socket.close()
	def set_response_header(self,status,headers):
		self.status = status
		self.headers = headers
	
	def run_forever(self):
		while True:
			new_socket,new_addr = self.tcp_server_socket.accept()
			p = multiprocessing.Process(target=self.server_client,args=(new_socket,))
			p.start()
			new_socket.close()
		self.tcp_server_socket.close()

def main():
	if len(sys.argv) == 2:
		try:
			port = int(sys.argv[1])
		except Exception as ret:
			print("端口输入错误")
			return
	else:
		print("请按照如下方式运行")
		print("python3 xxxx.py 7890")
		return
	wsgi_server = WSGIServer(port)
	wsgi_server.run_forever()

if __name__ == "__main__":
	main()
