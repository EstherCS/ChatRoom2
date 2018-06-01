# -*- encoding: utf-8 -*-
import socket
import threading
import time


class Server:
    def __init__(self, host, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock = sock
        self.sock.bind((host, port))
        self.sock.listen(5)
        print('Server', socket.gethostbyname(host), 'listening ...')
        self.mylist = list()

    def checkConnection(self):
        connection, addr = self.sock.accept()
        print('Accept a new connection', connection.getsockname(), connection.fileno())
        print("Online: ", len(self.mylist)+1, "user(s)")
        #self.tellOthers("Online",len(self.mylist)+1)
        try:
            buf = connection.recv(1024).decode()
            #if buf == '1':
                # start a thread for new connection
            temp = "SYSTEM: " + buf + " in the chat room." + " ," + "Online : " + str(len(self.mylist)+1)
            self.tellOthers("222", temp)
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

def main():
    s = Server('localhost', 5552)

    while True:
        s.checkConnection()


if __name__ == "__main__":
    main()

