import socket
import json


class Server:
    clients = {}

    def __init__(self):
        self._sock = None

    @staticmethod
    def _decode_message(message: bytes) -> dict:
        message_json = json.loads(message)
        return message_json

    def run(
        self,
        host: str = '0.0.0.0',
        port: int = 3000
    ) -> None:
        """Cria um servidor para
        troca e gerenciamento dos
        usuários.

        :param host: IP do host, o padrão é '0.0.0.0'
        :type host: str, optional
        :param port: Porta de escuta, o padrão é 3000
        :type port: int, optional
        """

        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._sock.bind((host, port))

        print('\033[1mChat Tkinter - @jaedsonpys\033[m')
        print('\033[32m     * Server is started\033[m')

        self._receive_connections()

    def _register_user(self, username: str, address: str,) -> None:
        self.clients[address] = username    
        print(f'    * {address} - Joined the chat')

    def _broadcast_message(self, message: str, sender_addr: str) -> None:
        sender = self.clients.get(sender_addr)

        message_info = {'type': 'message', 
                        'sender': sender,
                        'content': message}

        message_json = json.dumps(message_info, ensure_ascii=False)

        for addr in self.clients.keys():
            host, port = addr.split(':')
            address = (host, int(port))

            self._sock.sendto(message_json.encode(), address)

    def _receive_connections(self) -> None:
        while True:
            msg, addr = self._sock.recvfrom(5024)
            message = self._decode_message(msg)

            address = f'{addr[0]}:{addr[1]}'

            if message['type'] == 'register':
                username = message['username']
                self._register_user(username, address)
            elif message['type'] == 'message':
                content = message['content']
                self._broadcast_message(content, address)


if __name__ == '__main__':
    app = Server()
    app.run()
