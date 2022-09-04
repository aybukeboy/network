import socket
import threading

from RemoteTcpClientController import RemoteTcpClientController


class TcpServer:
    serverSocket = 0
    connectedClients = []
    client_listener_thread = 0
    is_client_listener_thread_alive = False
    is_started = False

    # disardaki siniflarin fonksiyonlarini saklar
    data_received_functions = []
    connection_established_functions = []
    connection_lost_functions = []

    def __init__(self):
        self.serverSocket = socket.socket()

    def start(self, port):
        s = self.serverSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        s.bind(('', int(port)))
        s.listen(5)

        # istemcileri kabul et
        self.is_client_listener_thread_alive = True
        self.client_listener_thread = threading.Thread(target=self.begin_to_accept_clients)
        self.client_listener_thread.start()
        self.is_started = True

    def begin_to_accept_clients(self):
        try:
            while self.is_client_listener_thread_alive:
                client_socket, addr = self.serverSocket.accept()
                connected_client = RemoteTcpClientController(self, client_socket, addr)
                self.connectedClients.append(connected_client)
                for func in self.connection_established_functions:
                    func(connected_client)
        except socket.error:
            self.is_client_listener_thread_alive = False

    def send(self, data):
        if not self.is_started:
            raise Exception("Server is closed!")

        for connectedClientController in self.connectedClients:
            try:
                connectedClientController.clientSocket.send(bytes(data, 'utf-8'))
            except socket.error:
                self.on_connection_lost(connectedClientController)

    def stop(self):
        for connectedClientController in self.connectedClients:
            connectedClientController.clientSocket.close()
        self.serverSocket.close()
        self.is_client_listener_thread_alive = False
        if self.client_listener_thread.is_alive():
            self.client_listener_thread.join()
        self.is_started = False

    # diger siniflar fonksiyonlarini alip data_received_functions'in icinde saklar
    def add_data_received_function(self, data_receive_func):
        self.data_received_functions.append(data_receive_func)

    def add_connection_established_function(self, connection_established_func):
        self.connection_established_functions.append(connection_established_func)

    def add_connection_lost_function(self, connection_lost_func):
        self.connection_lost_functions.append(connection_lost_func)

    def on_data_received(self, data):
        # data geldikten sonra, disardaki siniflarin fonksiyonlarina, data'yi parametre olarak vererek cagirir
        for func in self.data_received_functions:
            func(data)

    def on_connection_lost(self, remote_tcp_client):
        self.connectedClients.remove(remote_tcp_client)
        for func in self.connection_lost_functions:
            func(remote_tcp_client)

