import socket

#创建tcp的套接字
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #ipv4   tcp

#创建udp的套接字
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


#关闭套接字
s.close()
