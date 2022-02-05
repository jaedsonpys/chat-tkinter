import socket


class Client:
    def __init__(self) -> None:
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addr = ('192.168.0.111', 3000)

    def receive_broadcast(self):
        message = self._sock.recv(5024)
