#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
import json
import time

items = []


def main(page):
    print(page)
    url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
    # 这里数据只有三个是需要变的，分别是：jsonpCallback，w， searchid
    data = {'qqmusic_ver': 1298,
            'remoteplace': 'txt.yqq.lyric',
            'inCharset': 'utf8',
            'sem': 1, 'ct': 24, 'catZhida': 1, 'p': page,
            'needNewCode': 0, 'platform': 'yqq',
            'lossless': 0, 'notice': 0, 'format': 'jsonp', 'outCharset': 'utf-8', 'loginUin': 0,
            'jsonpCallback': 'MusicJsonCallback19507963135827455',
            'searchid': '98485846416392878',
            'hostUin': 0, 'n': 10, 'g_tk': 5381, 't': 7,
            'w': '周杰伦',
            'aggr': 0
            }

    headers = {'content-type': 'application/json',
               'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
    r = requests.get(url, params=data, headers=headers)
    time.sleep(3)
    # 截取 第35个字符到最后一个
    text = r.text[35:-1]
    # print(text)
    result = json.loads(text)
    if result['code'] == 0:
        for list in result['data']['lyric']['list']:
            item = {
                'albumname': list['albumname'],
                'content': list['content']
            }
            items.append(item)
        # print (list)
        print(items)


if __name__ == '__main__':
    # 页数最多为20 ，根据歌手的歌曲多少决定
    for i in range(1, 20):
        main(i)
