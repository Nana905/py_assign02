import socket
from threading import Thread
import time
class Sever:
    #初始化
    def __init__(self):
        self.sever=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sever.bind(("127.0.0.1",8989))
        self.sever.listen()
        self.clients=[]
        self.c_ip_name={}
        self.listen_to()

    #监听
    def listen_to(self):
        while True:
            sock, addr = self.sever.accept()
            data='连接服务器成功！请输入用户名'
            sock.send(data.encode('utf-8'))
            self.clients.append(sock)
            #每连接一个客户端创建一个线程
            Thread(target=self.deal_data,args=((sock,self.clients,self.c_ip_name,addr))).start()

    #用户对话的传递
    def deal_data(self,sock,clients,ip_name,addr):
        name=sock.recv(1024).decode('utf-8')
        print(type(name))
        ip_name[addr]=name
        for c in clients:
            data1=name+'进入聊天室'
            c.send(data1.encode())
        while True:
            try:
                recv_data=sock.recv(1024).decode()
            except Exception as result:
                break
            if(recv_data=='exit'):
                break
            for c in clients:
                c.send((ip_name[addr]+" "+time.strftime("%X")).encode())
                c.send(recv_data.encode())

    #关闭客户端
    def close_client(self,sock,addr):
        self.clients.remove(sock)
        sock.close()
        print(self.c_ip_name[addr]+'已经离开')
        for c in self.clients:
            c.send((self.c_ip_name[addr]+'已经离开').encode())


if __name__ == '__main__':
    Sever()









