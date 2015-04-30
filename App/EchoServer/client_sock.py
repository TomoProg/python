#-*- coding:utf-8 -*-
import socket
import sys

class ClientSock:
	""" クライアントソケットクラス """

	def __init__(self, host_ip, port):
		""" コンストラクタ """
		self.client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.host_ip = host_ip
		self.port = port
		self.connect_flag = False
	
	def Connect(self):
		""" 接続 """
		if self.connect_flag:
			return False

		try:
			self.client_sock.connect((self.host_ip, self.port))
			self.connect_flag = True
			return True
		except:
			self.connect_flag = False
			return False

	def Recv(self):
		""" 受信 """
		if self.connect_flag is False:
			return False

		try:
			recv_msg = self.accept_sock.recv(1024)
			return recv_msg
		except:
			return False

	def Send(self, sendmsg):
		""" 送信 """
		if self.connect_flag is False:
			return False
		
		try:
			self.client_sock.sendall(sendmsg)
			return True
		except:
			return False
		
	def Close(self):
		""" ソケットクローズ """
		try:
			self.client_sock.close()
			self.connect_flag = False
			return True
		except:
			return False

if __name__ == "__main__":
	cl_sock = ClientSock("127.0.0.1", 20000)
	
	if cl_sock.Connect() is False:
		print("Connect Error!!")
		sys.exit(1)

	print("Connect Success!!")
	while True:
		msg = input(">")
		cl_sock.Send(msg.encode('utf-8'))

	cl_sock.Close()
