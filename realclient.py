import socket
import threading
from PyQt4.QtCore import QThread, SIGNAL

class NewClient(QThread):

    def __init__(self):
        QThread.__init__(self)
        self.ip = "127.0.0.1"
        self.port = 4040
        self.isOffline = True
        self.data = 'go'

    def run(self):
        self.connect_to_server()

    def connect_to_server(self):
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serversocket.connect((self.ip, self.port))
        self.emit(SIGNAL("nowOnline()"))
        self.msg = self.serversocket.recv(2048)
        self.emit(SIGNAL("firstMessage(QString)"), self.msg)
        print("Greeting: "+self.msg)
        while self.data != 'exit':
            self.emit(SIGNAL("type_chat()"))
            # self.send_message()
            print("Waiting for response")
            self.msg = self.serversocket.recv(2048)
            self.emit(SIGNAL("new_msg(QString)"), self.msg)
            print("response: " + self.msg)

    def send_message(self, message):
        # self.data = raw_input("enter message: ")
        self.serversocket.send(bytes(message))
        print("sent!")

    def disconnect(self):
        self.data  = 'exit'
        self.isOffline = True
        self.serversocket.close()

