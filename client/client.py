import socket
import json


class Client:
    def __init__(self) -> None:
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addr = ('192.168.0.111', 3000)

    def send_message(self, message: str):
        message_json = json.dumps({'type': 'message',
                        'content': message}, ensure_ascii=False)

        self._sock.sendto(message.encode(), self.addr)

    def receive_broadcast(self):
        message = self._sock.recv(5024)
