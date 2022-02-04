import socket
from threading import Thread


class Server:
    conn_clients = []

    def __init__(self):
        self._sock = None

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

        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.bind((host, port))

        self._sock.listen(50)

        Thread(target=self._accept_connection).start()
        Thread(target=self._receive_messages).start()

    def _accept_connection(self) -> None:
        while True:
            client, addr = self._sock.accept()
            self.conn_clients.append(client)


if __name__ == '__main__':
    app = Server()
    app.run(host='127.0.0.1')
