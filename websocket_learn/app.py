#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import threading

import websocket


def on_ping(ws, data):
    print(f"Ping: {data}")


def on_pong(ws, data):
    print(f"Pong: {data}")


def on_message(ws, message):
    print(message)


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    def run(*args):
        for i in range(3):
            time.sleep(1)
            ws.send("Hello %d" % i)
        time.sleep(40)  # todo
        ws.close()
        print("thread and websocket terminating...")
    threading.Thread(target=run).start()


if __name__ == "__main__":
    # websocket.enableTrace(True)
    ws = websocket.WebSocketApp(
        "ws://echo.websocket.org/",
        on_ping=on_ping,
        on_pong=on_pong,
        on_error=on_error,
        on_close=on_close,
    )
    ws.on_open = on_open
    ws.on_message = on_message
    ws.run_forever()
