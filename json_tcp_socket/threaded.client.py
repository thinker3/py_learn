#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import socket
import random
import threading

from utils.common import (
    pack_json_object_to_length_comma_limited_stream,
    unpack_length_comma_limited_stream_to_json_objects,
)


def send_all(request, obj):
    request.sendall(pack_json_object_to_length_comma_limited_stream(obj, 'gbk'))


class SocketClient(object):
    def __init__(self, host, port):
        self.data = b''
        self.objs = []
        self.closed = False
        request = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        request.connect((host, port))
        self.request = request
        self.sender_thread = threading.Thread(target=self.send_by_interval)
        self.sender_thread.daemon = True
        self.sender_thread.start()

    def send_by_interval(self):
        while not self.closed:
            obj = {
                "num": random.randint(0, 9),
            }
            send_all(self.request, obj)
            time.sleep(1)

    def handle(self):
        while not self.closed:
            data = b''
            try:
                data = self.request.recv(1024)
            except ConnectionResetError as e:
                pass

            if not data:
                self.close()
                break
            print(f'Received from server >>> {data}')
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
        if obj.get('cmd') == 'exit':
            self.close()

    def close(self):
        self.closed = True
        self.request.close()


if __name__ == '__main__':
    host, port = "localhost", 8765
    threading.Thread(target=SocketClient(host, port).handle).start()
    threading.Thread(target=SocketClient(host, port).handle).start()
