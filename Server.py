# -*- encoding: utf-8 -*-
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QThread, pyqtSignal
from pymongo import MongoClient
import socket
import threading
import time
import serverui
import sys

class Server(QMainWindow, serverui.Ui_MainWindow):
    def __init__(self, host, port):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock = sock
        self.sock.bind((host, port))
        self.sock.listen(5)
        self._tutorial_thread = TutorialThread()
        self.connectmongoDB()
        print('Server', socket.gethostbyname(host), 'listening ...')
        self.mylist = list()
        self.Add.setText("Add")
        self.Add.clicked.connect(self.add)

    def connectmongoDB(self):
        self.client = MongoClient('localhost', 27017)  # 比较常用
        self.database = self.client["Chatroom"]  # SQL: Database Name
        self.collection = self.database["test"]  # SQL: Table Name

        for ii in self.collection.find():
            print(ii)
            self.SBody.append(ii['username'])
            self.SBody.update()

    def add(self):
        name = self.SInputName.text()
        password = self.SPassword.text()
        userList = []
        userList.append({'username': str(name), 'password': str(password)})
        print(userList)
        self.collection.insert_many(userList)
        self.SBody.append(name)
        self.SBody.update()

    def delete_data(self, unameList=None):
        name = self.SInputName.text()
        password = self.SPassword.text()

    def checkConnection(self):
        connection, addr = self.sock.accept()
        print('Accept a new connection', connection.getsockname(), connection.fileno())
        print("Online: ", len(self.mylist)+1, "user(s)")
        try:
            buf = connection.recv(1024).decode()
            #if buf == '1':
                # start a thread for new connection
            temp = "SYSTEM: " + buf + " in the chat room."
            self.tellOthers(connection.fileno(), temp)
            mythread = threading.Thread(target=self.subThreadIn, args=(connection, connection.fileno()))
            mythread.setDaemon(True)
            mythread.start()

            #else:
            #    connection.send(b'please go out!')
            #    connection.close()
        except:
            pass

    # send whatToSay to every except people in exceptNum
    def tellOthers(self, exceptNum, whatToSay):
        for c in self.mylist:
            if c.fileno() != exceptNum:
                try:
                    c.send(whatToSay.encode())
                except:
                    pass

    def subThreadIn(self, myconnection, connNumber):
        self.mylist.append(myconnection)
        while True:
            try:
                recvedMsg = myconnection.recv(1024).decode()
                if recvedMsg:
                    t= time.strftime("  [%H:%M:%S]",time.localtime())
                    self.tellOthers(connNumber, recvedMsg+t)
                else:
                    pass

            except (OSError, ConnectionResetError):
                try:
                    self.mylist.remove(myconnection)
                    print(len(self.mylist))
                except:
                    pass

                myconnection.close()
                return

class TutorialThread(QThread):
    received = pyqtSignal(str)

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def connect(self, host, port, name):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock = sock
        self.sock.connect((host, port))
        self.sock.send(name.encode())

    #receive server's send's others massages
    def run(self):
        while True:
            try:
                otherword = self.sock.recv(1024)  # socket.recv(recv_size)
                # print(otherword.decode())
                self.received.emit(otherword.decode())
            except ConnectionAbortedError:
                print('Server closed this connection!')

            except ConnectionResetError:
                print('Server is closed!')


class Main(QMainWindow, serverui.Ui_MainWindow):
     name = str  #save user name
     def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

     def connectmongoDB(self):
        self.client = MongoClient('localhost', 27017)  # 比较常用
        self.database = self.client["Chatroom"]  # SQL: Database Name
        self.collection = self.database["test"]  # SQL: Table Name

     def add_data(self,name=None, password=None):
        self.Add.setText("Add")
        self.Add.clicked.connect(self.add)

     def add(self):
        name = self.SInputName.text()
        password = self.SPassword.text()
        userList = []
        userList.append({'username': name, 'password': password})
        self.collection.insert_many(userList)
        self.SBody.append(name)
        self.SBody.update()

def main():
    #s = Server('localhost', 5552)
    # while True:
    #     s.checkConnection()
    app = QApplication(sys.argv)
    MainWindow = Server('localhost', 5552)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

    # s = Server('localhost', 5552)
    # while True:
    #     s.checkConnection()




