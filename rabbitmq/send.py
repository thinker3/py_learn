#!/usr/bin/env python
# encoding: utf-8

import pika
import time

# No handlers could be found for logger "pika.adapters.base_connection"
import logging
logging.basicConfig(level=logging.CRITICAL)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
for i in range(3):
    time.sleep(1)
    channel.basic_publish(exchange='', routing_key='hello', body=str(i))
    print "Sending %s" % i

connection.close()
