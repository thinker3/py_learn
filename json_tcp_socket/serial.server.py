#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import threading
import socketserver
from copy import copy

from utils.common import (
    pack_json_objects_to_length_comma_limited_stream,
    unpack_length_comma_limited_stream_to_json_objects,
)
from utils.log import get_logger
logger = get_logger(__name__)

from utils.redis_utils import get_redis_conn
redis_conn = get_redis_conn()

response_tpl = {
    "code": "1",
    "message": "",
}
login_request = {
    "cmd": "loginRequest",
}


def send_all(request, objs):
    request.sendall(pack_json_objects_to_length_comma_limited_stream(objs, 'gbk'))


class Consumer(threading.Thread):
    def __init__(self, request, device, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.flag = threading.Event()
        self.request = request
        self.device = device
        logger.debug(f'{request}: {self}')

    def run(self):
        while not self.flag.is_set():
            queue_name = f'request_list__{self.device}'
            value = redis_conn.rpop(queue_name)
            if value:
                try:
                    self.request.sendall(value)
                except OSError as e:
                    logger.error(f'Error: {e}; Value: {value}')
            time.sleep(0.1)


class MyTCPHandler(socketserver.BaseRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = b''
        self.objs = []
        self.request_thread_map = {}

    def handle_queue(self, device):
        thread = Consumer(self.request, device)
        thread.start()
        self.request_thread_map[self.request] = thread

    def close_thread(self):
        thread = self.request_thread_map.get(self.request)
        if thread:
            thread.flag.set()
            del self.request_thread_map[self.request]

    def handle(self):
        send_all(self.request, [login_request])
        while True:
            data = b''
            try:
                data = self.request.recv(1024)
            except ConnectionResetError as e:
                logger.error(e)
            if not data:
                self.close_thread()
                break
            ip, port = self.client_address
            logger.debug(f'Received from client {ip}:{port} >>> {data}')
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
        if obj.get('cmd') == 'login':
            device = obj['device']
            self.handle_queue(device)
        else:
            response = copy(response_tpl)
            response.update(cmd=obj.get('cmd', ''))
            send_all(self.request, [response])


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()
