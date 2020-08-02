#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import socket
import threading
import socketserver


def show_current_threads():
    while True:
        names = [thread.name for thread in threading.enumerate()]
        names = ', '.join(names)
        info = f"Active threads: {threading.active_count()}, {names}"
        print(info)
        time.sleep(1)


class MyThreadingTCPServer(socketserver.ThreadingTCPServer):
    def process_request_thread(self, request, client_address):
        super().process_request_thread(request, client_address)
        cur_thread = threading.current_thread()
        time.sleep(2)
        print(f"{cur_thread.name}: over")


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024).decode()
        cur_thread = threading.current_thread()
        response = f"{cur_thread.name}: {data}".encode()
        self.request.sendall(response)


if __name__ == "__main__":
    host, port = "localhost", 8765
    server = MyThreadingTCPServer((host, port), ThreadedTCPRequestHandler)
    t = threading.Thread(target=show_current_threads)
    t.daemon = True
    t.start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.shutdown()
