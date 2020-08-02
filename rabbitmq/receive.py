#!/usr/bin/env python
# encoding: utf-8

import pika

connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
print('Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print("Received %r" % (body,))

channel.basic_consume(callback, queue='hello', no_ack=True)
try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()

