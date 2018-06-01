from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QThread, pyqtSignal
import Clientui
from pymongo import MongoClient
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

    # check checkUserExist
    def checkUserExist(self, uname='A'):
        pass
        return False

    # query user bu uname
    # dbChatRoom.queryByuname(uname='A', upwd='A')
    def queryByuname(self, uname='A', upwd='A'):
        pass
        return False

    # Init database
    # dbChatRoom.Initdatabase()
    def Initdatabase(self):
        userList = []
        userList.append({'uname': 'A', 'upwd': 'A'})
        userList.append({'uname': 'B', 'upwd': 'B'})
        userList.append({'uname': 'C', 'upwd': 'C'})
        userList.append({'uname': 'D', 'upwd': 'D'})
        userList.append({'uname': 'E', 'upwd': 'E'})
        self.collection.insert_many(userList)

    def colseClient(self):
        self.client.close()


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

class Main(QMainWindow, Clientui.Ui_MainWindow):
    name = str  #save user name
    alreay = 0

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self._tutorial_thread = TutorialThread()
        self._tutorial_thread.received.connect(self.receive)

        self.connect_mongo()

        self.Login.setText("Login")
        self.Login.clicked.connect(self.login)
        # while(self.alreay == 0):
        #     self.Login.clicked.connect(self.login)

        self.UpdateP.setText("UpdatePassword")
        self.UpdateP.clicked.connect(self.changepassword)

        self.Send.setText("Send")
        self.Send.clicked.connect(self.send)
        self.Send.setEnabled(False)
        self.Text.setEnabled(False)

    def connect_mongo(self):
        self.client = MongoClient('localhost', 27017)  # 比较常用
        self.database = self.client["ChatRoom"]  # SQL: Database Name
        self.collection = self.database["user"]  # SQL: Table Name
        for ii in self.collection.find():
            print(ii)

    def check_account(self, username, pwd):
        if(self.collection.find({'uname': str(username), 'upwd': str(pwd)}) is not None):
            self.already = 1
            return False
        return True

    def changepassword(self):
        inputName = self.InputName.text()
        updatePassword = self.ChangePassword.text()
        print(inputName, updatePassword)
        dbChatRoom.updataUser(inputName, updatePassword)
        self.ChangePassword.setText("")
        self.UpdateP.setEnabled(False)

    def login(self):
        inputName = self.InputName.text()
        inputPassword = self.InputPassword.text()
        while(self.check_account(inputName, inputPassword)):
            return True

        print(inputName, inputPassword)
        dbChatRoom.insertUser(inputName, inputPassword)

        self.name = str(inputName)
        self.Body.append("Welcome to chat room! "+inputName)
        self.Body.update()
        self.Body.append("Now Lets Chat, "+inputName)
        self.Body.update()

        # self.InputName.setText("")
        # self.InputPassword.setText("")

        # self.InputName.setEnabled(False)
        # self.InputPassword.setEnabled(False)
        self.Login.setEnabled(False)
        self.Send.setEnabled(True)
        self.Text.setEnabled(True)

        #start to receive others massages
        self._tutorial_thread.connect('localhost', 5552, inputName)
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
    dbChatRoom = DataBaseChatRoom()
    # dbChatRoom.Initdatabase()
    dbChatRoom.colseClient()
    sys.exit(app.exec_())
