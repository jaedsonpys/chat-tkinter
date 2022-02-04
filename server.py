import socket
from threading import Thread

import json


class Server:
    clients = []

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

        Thread(target=self._receive_messages).start()

    def _receive_messages(self):
        while True:
            msg, client = self._sock.recvfrom(1024)
            message = self._decode_message(msg)

            if message['type'] == 'register':
                pass
            elif message['type'] == 'message':
                pass


if __name__ == '__main__':
    app = Server()
    app.run(host='127.0.0.1')
