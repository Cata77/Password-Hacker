import socket
import sys

ip_address = sys.argv[1]
port = sys.argv[2]
message = sys.argv[3]


class Socket:
    def __init__(self):
        self.sock = socket.socket()

    def connect(self, host, port):
        self.sock.connect((host, port))

    def send(self, message):
        self.sock.send(message.encode())

    def receive(self):
        return self.sock.recv(1024)

    def close_conn(self):
        self.sock.close()


def main():
    sock = Socket()
    sock.connect(ip_address, int(port))
    sock.send(message)
    print(sock.receive().decode('utf-8'))
    sock.close_conn()


if __name__ == '__main__':
    main()
