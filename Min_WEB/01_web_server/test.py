#coding-"UTF-8"
import time
import socket
import multiprocessing

class WSGIServer(object):
	def __init__(self):
		self.tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
		self.tcp_server_socket.bind(('192.168.0.106',7890))
	
	def run_forever(self):
		while True:
			new_sock,new_addr = self.tcp_server_socket.accept()
			print(new_sock)
			print(new_addr)





def main():
	wsgi_server = WSGIServer()
	wsgi_server.run_forever()

if __name__ == "__main__":
	main()
