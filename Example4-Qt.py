from PyQt5.QtWidgets import QMainWindow, QApplication
import assignment
import sys

class Main(QMainWindow, assignment.Ui_MainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.Login.setText("Login")
        self.Login.clicked.connect(self.login)

        self.Send.setText("Send")
        self.Send.clicked.connect(self.send)

    def login(self):
        text=self.InputName.text()
        #self.Body.append(text)
        #self.Body.update()
        #self.InputName.setText("")
        self.Body.append("Welcome to chat room! "+text)
        self.Body.update()
        self.Body.append("Now Lets Chat, "+text)
        self.Body.update()
        self.InputName.setText("")

    def send(self):
        text=self.Text.text()
        self.Body.append(text)
        self.Body.update()
        self.Text.setText("")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = Main()
    MainWindow.show()
    sys.exit(app.exec_())
