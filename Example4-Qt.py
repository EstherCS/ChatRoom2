from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QThread, pyqtSignal
from pymongo import MongoClient
import assignment
import sys
import socket
import time
import threading
class DataBaseChatRoom:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)  # 比较常用
        self.database = self.client["ChatRoom"]  # SQL: Database Name
        self.collection = self.database["user"]  # SQL: Table Name

    def loadData(self):
        pass
        return None

    # delete user by uname
    # dbChatRoom.deleteUser(['A'])
    def deleteUser(self, unameList=None):
        pass
        return 'successful'

    # insert user
    # dbChatRoom.insertUser(uname='A', upwd='A')
    def insertUser(self, uname, upwd):
        userList = []
        userList.append({'uname': uname, 'upwd': upwd})
        self.collection.insert(userList)
        print("success")

    def updataUser(self, uname, upwd):
        self.collection.remove({'uname': uname}) #remove account
        userList = []
        userList.append({'uname': uname, 'upwd': upwd})
        self.collection.insert(userList)

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

class Main(QMainWindow, assignment.Ui_MainWindow):
    name = str  #save user name
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self._tutorial_thread = TutorialThread()
        self._tutorial_thread.received.connect(self.receive)

        self.Login.setText("Login")
        self.Login.clicked.connect(self.login)
        
        self.UpdateP.setText("UpdatePassword")
        self.UpdateP.clicked.connect(self.changepassword)
        
        self.Send.setText("Send")
        self.Send.clicked.connect(self.send)
        self.Send.setEnabled(False)
        self.Text.setEnabled(False)

    def login(self):
        text=self.InputName.text()
        self.name = str(text)
        self.Body.append("Welcome to chat room! "+text)
        self.Body.update()
        self.Body.append("Now Lets Chat, "+text)
        self.Body.update()

        self.InputName.setText("")
        self.InputName.setEnabled(False)
        self.Login.setEnabled(False)
        self.Send.setEnabled(True)
        self.Text.setEnabled(True)

        #start to receive others massages
        self._tutorial_thread.connect('localhost', 5552, text)
        self.start()

    def start(self):
        self._tutorial_thread.start()

    def stop(self):
        self._tutorial_thread.terminate()


    def send(self):
        text=self.Text.text()
        self.Body.append("                                                              "+text+":You")
        self.Body.update()
        mes = self.name + ": "+ str(text)
        self._tutorial_thread.sock.send(mes.encode())
        self.Text.setText("")

    def receive(self, data):
        temp, temp2 = data.split(',', 1)
        self.Body.append(str(temp))
        self.Body.update()
        self.people.setText("")
        self.people.append(str(temp2))
        self.people.update()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = Main()
    MainWindow.show()
    sys.exit(app.exec_())
