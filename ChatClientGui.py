# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Client.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import socket
import time
import sys
import os
import realclient

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import SIGNAL


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(342, 311)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.textEdit = QtGui.QTextEdit(self.frame)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout.addWidget(self.textEdit)
        self.messageInput = QtGui.QLineEdit(self.frame)
        self.messageInput.setObjectName(_fromUtf8("messageInput"))
        self.verticalLayout.addWidget(self.messageInput)
        self.submitButton = QtGui.QPushButton(self.frame)
        self.submitButton.setObjectName(_fromUtf8("submitButton"))
        self.verticalLayout.addWidget(self.submitButton)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 342, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuConnection = QtGui.QMenu(self.menubar)
        self.menuConnection.setObjectName(_fromUtf8("menuConnection"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionDisconnect = QtGui.QAction(MainWindow)
        self.actionDisconnect.setObjectName(_fromUtf8("actionDisconnect"))
        self.actionConnect = QtGui.QAction(MainWindow)
        self.actionConnect.setObjectName(_fromUtf8("actionConnect"))
        self.menuConnection.addAction(self.actionDisconnect)
        self.menuConnection.addAction(self.actionConnect)
        self.menubar.addAction(self.menuConnection.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #some personal code added to this 
        self.actionConnect.triggered.connect(self.connect_to_server)
        self.actionDisconnect.triggered.connect(self.disconnect_server)

        self.submitButton.clicked.connect(self.send_message)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Secured chat client", None))
        self.submitButton.setText(_translate("MainWindow", "SEND MESSAGE", None))
        self.menuConnection.setTitle(_translate("MainWindow", "Connection", None))
        self.actionDisconnect.setText(_translate("MainWindow", "Disconnect", None))
        self.actionConnect.setText(_translate("MainWindow", "Connect", None))

    def connect_to_server(self):
        print("make connection to the server")
        self.submitButton.setEnabled(False)
        self.client = realclient.NewClient()
        self.connect(self.client, SIGNAL("nowOnline()"), self.is_online)
        self.connect(self.client, SIGNAL('firstMessage(QString)'), self.first_message)
        self.connect(self.client, SIGNAL('type_chat()'), self.do_write_chat)
        self.connect(self.client, SIGNAL("new_msg(QString)"), self.update_new_chat)
        self.client.start()

    def do_write_chat(self):
        print("Now you can write your chat")
        self.submitButton.setEnabled(True)

    def disconnect_server(self):
        self.client.disconnect()
        self.actionConnect.setEnabled(True)
        self.actionDisconnect.setEnabled(False)
        print("disconnected fromm the server")

    def update_new_chat(self, chatvalue):
        print("client message: "+ self.client.msg)
        self.textEdit.setText(self.textEdit.toPlainText() + "\n"+str(chatvalue).decode('utf-8'))
        print("you have a new chat")

    def send_message(self):
        message = "Client: > " + self.messageInput.text()
        print("YOu typed : " + message)
        self.client.send_message(message)
        self.textEdit.setText(self.textEdit.toPlainText() + "\n"+message)
        self.messageInput.setText('')
        self.submitButton.setEnabled(False)
        print("message sent to the server")

    def is_online(self):
        QtGui.QMessageBox.information(self, "Done!", "You are now connected to server!")
        MainWindow.setWindowTitle("Connected")
        self.actionConnect.setEnabled(False)

    def first_message(self, greeting):
        self.textEdit.setText(greeting)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

