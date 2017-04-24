# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChatServer.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import socket
import time
import sys
import os
import realserver

from PyQt4 import QtGui,QtCore
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
        MainWindow.resize(308, 296)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.formLayout_2 = QtGui.QFormLayout(self.centralwidget)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.formLayout = QtGui.QFormLayout(self.frame)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.msgOutput = QtGui.QTextBrowser(self.frame)
        self.msgOutput.setObjectName(_fromUtf8("msgOutput"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.SpanningRole, self.msgOutput)
        self.msgInput = QtGui.QLineEdit(self.frame)
        self.msgInput.setObjectName(_fromUtf8("msgInput"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.msgInput)
        self.msgButton = QtGui.QPushButton(self.frame)
        self.msgButton.setObjectName(_fromUtf8("msgButton"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.msgButton)
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.frame)
        self.conStatus = QtGui.QLabel(self.centralwidget)
        self.conStatus.setObjectName(_fromUtf8("conStatus"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.conStatus)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 308, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuServer = QtGui.QMenu(self.menubar)
        self.menuServer.setObjectName(_fromUtf8("menuServer"))
        self.menuApplication = QtGui.QMenu(self.menubar)
        self.menuApplication.setObjectName(_fromUtf8("menuApplication"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionStart_Server = QtGui.QAction(MainWindow)
        self.actionStart_Server.setObjectName(_fromUtf8("actionStart_Server"))
        self.actionStop_Server = QtGui.QAction(MainWindow)
        self.actionStop_Server.setObjectName(_fromUtf8("actionStop_Server"))
        self.actionExit_app = QtGui.QAction(MainWindow)
        self.actionExit_app.setObjectName(_fromUtf8("actionExit_app"))
        self.actionInsert_key = QtGui.QAction(MainWindow)
        self.actionInsert_key.setObjectName(_fromUtf8("actionInsert_key"))
        self.menuServer.addSeparator()
        self.menuServer.addAction(self.actionStart_Server)
        self.menuServer.addAction(self.actionStop_Server)
        self.menuServer.addAction(self.actionInsert_key)
        self.menuApplication.addAction(self.actionExit_app)
        self.menubar.addAction(self.menuServer.menuAction())
        self.menubar.addAction(self.menuApplication.menuAction())

        #my added lines for actions 
       	self.actionExit_app.triggered.connect(self.close_application)

       	#my added lines for button events
       	self.msgButton.clicked.connect(self.send_message)

        #my action for starting the server
        self.actionStart_Server.triggered.connect(self.start_server)
        self.actionStop_Server.triggered.connect(self.disconnect)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Secure Chat", None))
        self.msgButton.setText(_translate("MainWindow", "SEND MESSAGE", None))
        self.conStatus.setText(_translate("MainWindow", "Offline", None))
        self.menuServer.setTitle(_translate("MainWindow", "Server", None))
        self.menuApplication.setTitle(_translate("MainWindow", "Application", None))
        self.actionStart_Server.setText(_translate("MainWindow", "Start Server", None))
        self.actionStop_Server.setText(_translate("MainWindow", "Stop Server", None))
        self.actionExit_app.setText(_translate("MainWindow", "Exit app", None))
        self.actionInsert_key.setText(_translate("MainWindow", "Insert key", None))

    def close_application(self):
    	print("this is closing the application")

    def start_server(self):
    	print("starting the application")
        self.msgButton.setEnabled(False)
        self.server = realserver.NewServer()
        self.connect(self.server, SIGNAL('nowOnline()'), self.now_online)
        self.connect(self.server, SIGNAL('new_chat(QString)'), self.new_message)
        self.connect(self.server, SIGNAL('write_chat()'), self.write_chat)
        self.server.start()

    def send_message(self):
        message = "Server: > " + self.msgInput.text()
        self.server.send_message(message)
        #upadte the textOutput with the current typed message
        print("outside send: " + message)
        self.msgOutput.setText(self.msgOutput.toPlainText()+"\n"+message)
        #then remove the text in the textbox 
        self.msgInput.setText('')
        self.msgButton.setEnabled(False)
        # print(self.server.client)
        print("message by buttonn")

    def write_chat(self):
        ''' user writes in textbox then click button to send message '''
        # message = self.msgInput.text()
        self.msgButton.setEnabled(True)
        print("now you can write in the box")

    def insert_key(self, message):
        print("insert: " + self.server.data)
        newmsg = QtCore.QString(message)
        print("new; " + newmsg)
        self.msgOutput.append(newmsg)
        print("now insert the key")

    def new_message(self, value):
        print("there is a new chat item")
        print("outside new: " + value)
        print(str(value), len(str(value)))
        print("\nds : " + QtCore.QString(self.server.data))
        self.msgOutput.setText(self.msgOutput.toPlainText() + 
            "\n"+str(value).decode('utf-8'))


    def now_online(self):
        QtGui.QMessageBox.information(self, "Done!", "Server is now online !")
        self.conStatus.setText("Online")
        self.actionStart_Server.setEnabled(False)

    def disconnect(self):
        self.actionStart_Server.setEnabled(True)
        self.actionStop_Server.setEnabled(False)
        self.server.disconnect()



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

