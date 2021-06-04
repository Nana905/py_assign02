import socket
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from threading import Thread
class Clients(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        pa=QtGui.QPalette()
        #背景
        bg=QtGui.QPixmap(r"./背景图片.png")
        pa.setBrush(self.backgroundRole(),QtGui.QBrush(bg))
        self.setPalette(pa)

        #聊天窗口
        self.window=QTextBrowser(self)
        self.window.move(30,50)
        self.window.resize(500,200)

        # 发送信息行
        self.text = QLineEdit(self)
        self.text.setPlaceholderText('请输入你想发送的内容')
        self.text.move(30, 300)
        self.text.resize(500, 30)

        #发送按钮
        self.button = QPushButton('发送', self)
        self.button.move(380, 350)

        self.client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.client.connect(('127.0.0.1',8989))

        self.thread()

    #发送
    def send_message(self):
        message=self.text.text()
        self.client.send(message.encode('utf8'))
        if message=='exit':
            self.client.close()
            self.destroy() #关闭窗口
        self.text.clear()
        self.button.clicked.connect(self.send_message)

    #接收
    def recv_message(self):
        while True:
            try:
                recv_data=self.client.recv(1024).decode('utf8')
                print(recv_data)
                recv_data=recv_data+'\n'
                self.window.append(recv_data)
            except Exception as a:
                exit(0)

    #双线程
    def thread(self):
        Thread(target=self.send_message).start()
        Thread(target=self.recv_message).start()


if __name__ == '__main__':
    app=QApplication([])
    client=Clients()
    client.show()
    app.exec()