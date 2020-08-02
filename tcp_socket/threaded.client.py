#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket


def client(ip, port, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((ip, port))
        sock.sendall(message.encode())
        address = sock.getsockname()
        response = sock.recv(1024).decode()
        print(f"{address} received: {response}")


if __name__ == '__main__':
    ip, port = "localhost", 8765
    for i in range(5):
        client(ip, port, f"Hello World {i}")
