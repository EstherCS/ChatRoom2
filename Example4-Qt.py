from PyQt5.QtWidgets import QMainWindow, QApplication
import assignment
import sys

class Main(QMainWindow, assignment.Ui_MainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.Send.setText("Send")
        self.Send.clicked.connect(self.send)

    def send(self):
        text=self.lineEdit.text()
        self.Body.append(text)
        self.Body.update()
        self.Text.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = Main()
    MainWindow.show()
    sys.exit(app.exec_())
