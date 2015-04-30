#-*- coding:utf-8 -*-
import socket
import sys

class ServerSock:
	""" サーバソケットクラス """

	def __init__(self, host_ip, port):
		""" コンストラクタ """
		self.server_sock = None
		self.accept_sock = None
		self.accept_addr = None
		self.host_ip = host_ip
		self.port = port
		self.accept_flag = False
		self.init_flag = False
	
	def Init(self):
		""" サーバソケット初期化 """
		try:
			self.server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			self.server_sock.bind((self.host_ip, self.port))
			self.server_sock.listen(5)
			self.init_flag = True
			return True
		except:
			self.init_flag = False
			return False

	def Accept(self):
		""" 接続受信 """
		if self.init_flag is False:
			return False

		try:
			self.accept_sock, self.accept_addr = self.server_sock.accept()
			self.accept_flag = True
			return True
		except:
			self.accept_flag = False
			return False

	def Recv(self):
		""" 受信 """
		if self.accept_flag is False:
			return False

		try:
			recv_msg = self.accept_sock.recv(1024)
			return recv_msg
		except:
			return False

	def Send(self, sendmsg):
		""" 送信 """
		if self.accept_flag is False:
			return False
		try:
			self.accept_sock.sendall(sendmsg)
			return True
		except:
			return False
			
	def AcceptSockClose(self):
		""" アクセプトソケットクローズ """
		if self.accept_flag is False:
			return True

		try:
			self.accept_sock.close()
			self.accept_flag = False
			return True
		except:
			return False

	def ServerSockClose(self):
		""" サーバソケットクローズ """
		if self.init_flag is False:
			return True

		try:
			self.server_sock.close()
			self.init_flag = False
			return True
		except:
			return False

if __name__ == "__main__":
	server_sock = ServerSock("127.0.0.1", 20000)

	if server_sock.Init() is False:
		print("Init Failed...")
		sys.exit(1)

	print("Waiting for connections...")

	if server_sock.Accept() is False:
		print("Accept Failed...")
		sys.exit(1)

	print("Accept Success!!")
	while True:
		msg = server_sock.Recv()
		print(msg)
		if msg == False or msg == b"":
			break

	server_sock.AcceptSockClose()
	server_sock.ServerSockClose()
