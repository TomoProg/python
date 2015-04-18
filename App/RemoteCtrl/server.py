#-*- coding:utf-8 -*-

import socketserver
import sys
import os

class RemoteCtrlServer(socketserver.BaseRequestHandler):
	""" 遠隔操作サーバプログラム """

	def handle(self):
		print("Connected")
		while(True):
			command = input(">")
			command = command.strip()
			if len(command) > 0:
				self.request.sendall(command.encode('utf-8'))
		
if __name__ == "__main__":
	""" main """

	# Check Command Line
	args = sys.argv
	argc = len(args)
	if argc != 3:
		print("Usage: %s HOST_IP BIND_PORT" % args[0])
		sys.exit(1)

	HOST, PORT = args[1], int(args[2])
	server = socketserver.TCPServer((HOST, PORT), RemoteCtrlServer)
	print("Server Start!!")
	server.serve_forever()
