#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-22 21:18:50
# @Author  : ljljlhj (ljljlhj@foxmail.com)
# @Link    : ${link}
# @Version : $Id$

'''
需求：
分析豆果美食数据包
通过python多线程-线程池抓取数据
通过使用ip代理来隐藏数据
将书库保存到mongodb中

'''

import requests
import json

s = requests.session()


def handler_request(url, data):
    headers = {
        'client': '4',
        'version': '6932.2',
        'device': 'SM-G955F',
        'sdk': '19,4.4.2',
        'imei': '355757010176523',
        'channel': 'baidu',
        # 'mac': ' B0:52:16:0F:6A:DB',
        'resolution': '720*1280',
        'dpi': '1.5',
        # 'android-id': ' b052160f6adb3550',
        # 'pseudo-id': ' 60f6adb3550b0521',
        'brand': 'samsung',
        'scale': '1.5',
        'timezone': '28800',
        'language': 'zh',
        'cns': '3',
        'carrier': 'eMobile',
        # 'imsi': ' 440001765216151',
        'user-agent': 'Mozilla/5.0 (Linux; Android 4.4.2; SM-G955F Build/JLS36C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36',
        'reach': '1',
        'newbie': '0',
        'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
        'Accept-Encoding': 'gzip,deflate',
        'Connection': 'Keep-Alive',
        # 'Cookie': ' duid=58895586',
        'Host': 'api.douguo.net',
        # 'Content-Length': ' 74',
    }
    response = s.post(url=url, headers=headers, data=data)
    return response


def main():
    url = 'http://api.douguo.net/personalized/home'
    data = {
        'client': '4',
        '_session': '1550844954436355757010176523',
        'v': '1550747913',
        '_vs': '2305',
    }
    response = handler_request(url, data)
    print(response.text)


if __name__ == '__main__':
    main()
