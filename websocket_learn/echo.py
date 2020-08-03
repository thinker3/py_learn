#!/usr/bin/env python
# -*- coding: utf-8 -*-

import websocket


def short_lived_one_transfer():
    ws = websocket.create_connection("ws://echo.websocket.org/")
    ws.send("Hello, World")
    result = ws.recv()
    print(f'Received: {result}')
    assert ws.getstatus() == 101
    assert ws.gettimeout() is None
    assert ws.getsubprotocol() is None
    print(ws.sock.getsockname())
    print(ws.sock.getpeername())
    print(ws.getheaders())
    ws.close()
    return


if __name__ == '__main__':
    short_lived_one_transfer()
