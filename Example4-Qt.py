from PyQt5.QtWidgets import QMainWindow, QApplication
import assignment
import sys
import socket
import threading

class Main(QMainWindow, assignment.Ui_MainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.Login.setText("Login")
        self.Login.clicked.connect(self.login)

        self.Send.setText("Send")
        self.Send.clicked.connect(self.send)
        self.Send.setEnabled(False)
        self.Text.setEnabled(False)

    def login(self):
        text=self.InputName.text()
        #self.Body.append(text)
        #self.Body.update()
        #self.InputName.setText("")
        self.Body.append("Welcome to chat room! "+text)
        self.Body.update()
        self.Body.append("Now Lets Chat, "+text)
        self.Body.update()
        c = Client('localhost', 5550, text)
        #main(text)
        self.InputName.setText("")
        self.InputName.setEnabled(False)
        self.Login.setEnabled(False)
        self.Send.setEnabled(True)
        self.Text.setEnabled(True)
        #th1 = threading.Thread(target=c.sendThreadFunc,args=(text,))
        #th2 = threading.Thread(target=c.recvThreadFunc)
        #threads = [th1, th2]
        #for t in threads:
        #    t.setDaemon(True)
        #    t.start()
        #t.join()


    def send(self):
        text=self.Text.text()
        self.Body.append("                                                              "+text)
        self.Body.update()
        #self.sock.send(text.encode())
        self.Text.setText("")

class Client:
    def __init__(self, host, port, name):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock = sock
        self.sock.connect((host, port))
        self.sock.send(name.encode())

    def sendThreadFunc(self,name):
        while True:
            try:
                myword = name + ":" + input()
                self.sock.send(myword.encode())

            except ConnectionAbortedError:
                print('Server closed this connection!')
            except ConnectionResetError:
                print('Server is closed!')

    def recvThreadFunc(self):
        while True:
            try:
                otherword = self.sock.recv(1024) # socket.recv(recv_size)
                print(otherword.decode())
            except ConnectionAbortedError:
                print('Server closed this connection!')

            except ConnectionResetError:
                print('Server is closed!')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = Main()
    MainWindow.show()
    sys.exit(app.exec_())
