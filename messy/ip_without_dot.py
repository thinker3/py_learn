#!/usr/bin/env python
# encoding: utf-8


def int_to_binary_string(i):
    #i = "{0:b}".format(i)
    # with leading zeros
    i = "{:08b}".format(i)
    return i


def convert(ip):
    ip = map(int, ip.split('.'))
    ip = map(int_to_binary_string, ip)
    ip = ''.join(ip)
    print ip
    ip = int(ip, 2)  # binary string to int
    print 'http://%s/' % ip


def main():
    ip = '123.125.114.144'
    convert(ip)


if __name__ == '__main__':
    main()
