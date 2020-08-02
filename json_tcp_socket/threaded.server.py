#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import socket
import threading
import socketserver

from utils.common import (
    pack_json_object_to_length_comma_limited_stream,
    unpack_length_comma_limited_stream_to_json_objects,
)


def send_all(request, obj):
    request.sendall(pack_json_object_to_length_comma_limited_stream(obj))


class MyThreadingTCPServer(socketserver.ThreadingTCPServer):
    pass


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    def __init__(self, *args, **kwargs):
        self.data = b''
        self.objs = []
        super().__init__(*args, **kwargs)

    def handle(self):
        while True:
            data = b''
            try:
                data = self.request.recv(1024)
            except ConnectionResetError as e:
                pass
            if not data:
                break
            host, port = self.client_address
            print(f'Received from client {host}:{port} >>> {data}')
            self.data += data
            self.analysis()

    def analysis(self):
        objs, remained = unpack_length_comma_limited_stream_to_json_objects(self.data, 'gbk')
        self.data = remained
        for obj in objs:
            self.objs.append(obj)

        while len(self.objs):
            obj = self.objs.pop(0)
            self.respond(obj)

    def respond(self, obj):
        if obj.get('num') == 0:
            response = {
                "cmd": "exit",
            }
            send_all(self.request, response)


if __name__ == "__main__":
    host, port = "localhost", 8765
    server = MyThreadingTCPServer((host, port), ThreadedTCPRequestHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.shutdown()
