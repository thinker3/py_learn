#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import socket
import threading
from utils.common import (
    pack_json_objects_to_length_comma_limited_stream,
    unpack_length_comma_limited_stream_to_json_objects,
)
from utils.log import get_logger
logger = get_logger(__name__)

heart_beat = {
    "cmd": "heartbeat",
}
login = {
    "cmd": "login",
    "jcyxm": "王小明",
    "jcybh": "JCY005",
}


def send_all(request, objs):
    request.sendall(pack_json_objects_to_length_comma_limited_stream(objs, 'gbk'))


class RealSender(threading.Thread):
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.flag = threading.Event()
        self.request = request

    def run(self):
        while not self.flag.is_set():
            self.send_real()
            time.sleep(5)

    def send_real(self):
        obj = {
            "cmd": "real",
            "device": "dev001",
            "vin": "VIN123456",
            "plate": "川A12345",
        }
        send_all(self.request, [obj])


class SocketClient(object):
    def __init__(self, device):
        self.device = device
        request = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        request.connect(('0.0.0.0', 9999))
        self.request = request
        self.real_sender = RealSender(request)
        self.closed = False
        self.data = b''
        self.objs = []

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
            logger.debug(f'Received from server >>> {data}')
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
        if obj.get('cmd') == 'sendReal':
            if obj.get('accept') is True:
                self.real_sender.start()
            else:
                self.close()
        elif obj.get('cmd') == 'loginRequest':
            login.update(device=self.device)
            send_all(self.request, [login])

    def close(self):
        self.real_sender.flag.set()
        self.closed = True
        self.request.close()


if __name__ == '__main__':
    device = sys.argv[1]
    SocketClient(device).handle()
