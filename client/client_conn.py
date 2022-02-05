import socket
import json


class Client:
    def __init__(self) -> bool:
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.addr = ('192.168.0.111', 3000)

        # ping server
        ping = json.dumps({'type': 'ping'})
        self._sock.sendto(ping.encode(), self.addr)

        # wait response
        self._sock.settimeout(3.0)
        pong = self._sock.recv(1024).decode()

        if pong != 'pong':
            return False

        return True

    def register_user(self, username: str):
        message_json = json.dumps({'type': 'register', 'username': username}, ensure_ascii=False)
        self._sock.sendto(message_json.encode(), self.addr)

    def send_message(self, message: str):
        message_json = json.dumps({'type': 'message',
                        'content': message}, ensure_ascii=False)

        self._sock.sendto(message_json.encode(), self.addr)

    def receive_broadcast(self):
        message = json.loads(self._sock.recv(5024))
        
        sender = message['sender']
        content = message['content']

        return (sender, content)
