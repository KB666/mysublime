#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-14 15:25:25
# @Author  : ljljlhj (ljljlhj@foxmail.com)
# @Link    : ${link}
# @Version : $Id$

'''url = 'https://www.thepaper.cn/load_search.jsp?k=%E9%9D%9E%E6%B4%B2%E7%8C%AA%E7%98%9F&pagesize=10&searchPre=all_0:&orderType=3&pageidx=2'''

import requests
import json
import time

items = []


def handler_request(url):
    headers = {
        'Cookie': 'tt_webid=6679649988912825870; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6679649988912825870; __tasessionId=n5s0j452k1555228086451; s_v_web_id=cc45877e357dd3b93ae1f4c313b16667',
        'Referer': 'https://www.toutiao.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',

    }
    r = requests.get(url=url, headers=headers)
    return r


def parse(r):
    title_json = json.loads(r.text)
    title_list = title_json["data"]
    return title_list


def main():
    for page in range(0, 12):
        url = 'https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset={}&format=json&keyword=%E9%9D%9E%E6%B4%B2%E7%8C%AA%E7%98%9F&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis&timestamp=1555228460322'
        url = str(url.format(page * 20))
        time.sleep(3)
        r = handler_request(url)
        r.encoding = r.apparent_encoding
        lis = parse(r)
        for title_l in lis:
            try:
                title = title_l["title"]
                items.append(title)
                print(title)
            except Exception as e:
                print("脏数据已过滤")
    fp = open('头条.txt', 'w', encoding='utf8')
    for item in items:
        fp.write(str(item) + '\n')
    print('文件写入完成...........')
    fp.close()


if __name__ == '__main__':
    main()
