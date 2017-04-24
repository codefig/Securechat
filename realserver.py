import socket
import threading
import struct
from PyQt4.QtCore import QThread, SIGNAL

class NewServer(QThread):

	def __init__(self):
		QThread.__init__(self)
		self.clientlist = []
		self.ip = "127.0.0.1"
		self.port = 4040
		self.data = "sent"
		self.isOffline = True
		self.clientConnected = False

	def start_server(self):
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.server.bind((self.ip, self.port))
		self.server.listen(10)
		print("server started...")
		self.emit(SIGNAL('nowOnline()'))
		self.client, self.addr = self.server.accept()
		self.client.send("Welcome to the server")
		# self.data = self.client.recv(2048)
		while self.data != 'exit':
			print("waiting for reply\n")
			self.data = self.client.recv(2048)
			print("inside: " + self.data)
			self.emit(SIGNAL('new_chat(QString)'), self.data)
			print("client said : " + self.data)
			# emit signal for the server to type his msg
			self.emit(SIGNAL('write_chat()'))


	def run(self):
		self.start_server()

	def send_message(self, message):
		# self.msg = raw_input("enter your message: ")
		self.msg = message
		self.client.send(bytes(message))
		print("message sent")

	def disconnect(self):
		print("about to close connections..")
		self.client.close()
		self.server.close()
		print("Connections closed...")





