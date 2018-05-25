import socket
import threading

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

def main():
    print("Welcome to chat room!")
    name = input("Input your nickname : ")
    print("Now Let's Chat, ",name)
    c = Client('localhost', 5550, name)

    #self.sock.send(name.encode())
    th1 = threading.Thread(target=c.sendThreadFunc,args=(name,))
    th2 = threading.Thread(target=c.recvThreadFunc)
    threads = [th1, th2]
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()

if __name__ == "__main__":
    main()
