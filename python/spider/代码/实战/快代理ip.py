#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-27 17:00:27
# @Author  : ljljlhj (ljljlhj@foxmail.com)
# @Link    : ${link}
# @Version : $Id$

import requests
import re

lis = []


def handler_request(page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134', }
    url = 'https://www.kuaidaili.com/ops/proxylist/'
    url = url + str(page) + '/'
    r = requests.get(url=url, headers=headers)
    return r


def parse(r):
    string = r.text
    patternip = re.compile(r'<td data-title="IP">(.*?)</td>')
    patternport = re.compile(r'<td data-title="PORT">(.*?)</td>')
    ip = patternip.findall(string)
    port = patternport.findall(string)
    return(ip, port)


def savefile(ip, port):
    filename = 'proxy.txt'
    with open(filename, 'a') as fp:
        for i in range(0, len(ip)):
            fp.write(str(ip[i]) + ':' + str(port[i]) + '\n')


def main():
    for page in range(1, 10):
        r = handler_request(page)
        ip, port = parse(r)
        savefile(ip, port)


if __name__ == '__main__':
    main()
