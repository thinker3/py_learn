#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from utils.common import (
    pack_json_objects_to_length_comma_limited_stream,
)
from utils.log import get_logger
logger = get_logger(__name__)

from utils.redis_utils import get_redis_conn
redis_conn = get_redis_conn()

send_real_true = {
    "cmd": "sendReal",
    "accept": True,
    "interval": 1000,
}
send_real_false = {
    "cmd": "sendReal",
    "accept": False,
    "interval": 1000,
}


class Commander(object):
    def __init__(self, queue_name):
        self.started = False
        self.stopped = False
        self.queue_name = queue_name

    def run(self):
        text = ''
        while text != 'exit':
            text = input("Please input command > ")
            if text == 'send_real_true':
                if not self.started:
                    self.send_real_true_to_queue()
                    self.started = True
            elif text == 'send_real_false':
                if not self.stopped:
                    self.send_real_false_to_queue()
                    self.stopped = True

    def send_real_true_to_queue(self):
        stream = pack_json_objects_to_length_comma_limited_stream([send_real_true], 'gbk')
        redis_conn.lpush(self.queue_name, stream)

    def send_real_false_to_queue(self):
        stream = pack_json_objects_to_length_comma_limited_stream([send_real_false], 'gbk')
        redis_conn.lpush(self.queue_name, stream)


if __name__ == '__main__':
    device = sys.argv[1]
    queue_name = f'request_list__{device}'
    Commander(queue_name).run()
