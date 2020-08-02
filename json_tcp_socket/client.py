#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
from utils.common import (
    pack_json_objects_to_length_comma_limited_stream,
)
from utils.log import get_logger
logger = get_logger(__name__)

data = [
    {
        "cmd": "login",
        "username": "chenkun",
        "password": "123456",
    },
    {
        "cmd": "real",
        "device": "dev001",
        "vin": "VIN123456",
        "plate": "川A12345",
    },
]
data = pack_json_objects_to_length_comma_limited_stream(data, encoding='gbk')
logger.debug(data)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('0.0.0.0', 9999))
sock.settimeout(0.1)
sock.send(data)
sock.close()
