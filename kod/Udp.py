import socket
import threading


class Udp:
    remoteEndPoint = ('127.0.0.1', 0)
    listen_port = 13000
    data_listener_thread = 0
    is_data_listener_thread_alive = False
    is_opened = False

    # disardaki siniflarin fonksiyonlarini saklar
    data_received_functions = []

    def __init__(self):
        self.udpSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    def open(self, listen_port, ip, send_port):
        self.listen_port = listen_port
        self.remoteEndPoint = (ip, int(send_port))
        self.udpSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.udpSocket.bind(('', int(listen_port)))
        self.is_data_listener_thread_alive = True
        self.data_listener_thread = threading.Thread(target=self.begin_to_receive)
        self.data_listener_thread.start()
        self.is_opened = True

    def close(self):
        self.udpSocket.close()
        self.is_data_listener_thread_alive = False
        if self.data_listener_thread.is_alive():
            self.data_listener_thread.join()
        self.is_opened = False

    def send(self, data):
        if not self.is_opened:
            raise Exception("Port is closed!")
        self.udpSocket.sendto(bytes(data, 'utf-8'), self.remoteEndPoint)

    # diger siniflar fonksiyonlarini alip data_received_functions'in icinde saklar
    def add_data_received_function(self, data_receive_func):
        self.data_received_functions.append(data_receive_func)

    def begin_to_receive(self):
        while self.is_data_listener_thread_alive:
            try:
                data, address = self.udpSocket.recvfrom(1024)

                if data == b'':
                    self.is_data_listener_thread_alive = False
                    self.udpSocket.close()
                    break

                for func in self.data_received_functions:
                    func(data)

            except socket.error as exp:
                if "[WinError 10054]" not in str(exp):
                    self.is_data_listener_thread_alive = False
                    self.udpSocket.close()
                    self.is_opened = False
