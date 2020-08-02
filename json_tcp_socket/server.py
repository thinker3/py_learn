#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socketserver

from utils.common import (
    unpack_length_comma_limited_stream_to_json_objects,
)
from utils.log import get_logger
logger = get_logger(__name__)


class MyTCPHandler(socketserver.BaseRequestHandler):
    objs = []

    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).strip()
            except ConnectionResetError:
                self.data = ''
            if not self.data:
                break
            print(f'{self.client_address} wrote: {self.data}')
            logger.debug(self.data)
            self.analysis()
            print(self.objs)
            self.request.sendall(self.data.upper())

    def analysis(self):
        objs = unpack_length_comma_limited_stream_to_json_objects(self.data, 'gbk')
        for obj in objs:
            print(obj)
            self.objs.append(obj)


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()
