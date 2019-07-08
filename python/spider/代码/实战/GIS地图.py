#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-28 18:13:59
# @Author  : ljljlhj (ljljlhj@foxmail.com)
# @Link    : ${link}
# @Version : $Id$

import requests
from lxml import etree
import time
import os
# 'url = 'http://webmap.iwmi.org/arcgis/rest/services''


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
    'Connection': 'close',
}


def geturl(url):
    r = requests.get(url=url, headers=headers)
    tree = etree.HTML(r.text)
    lis = tree.xpath('//li/a/@href')
    return lis


def handel_request(url):
    url = 'http://webmap.iwmi.org' + url
    r = requests.get(url=url, headers=headers)
    tree = etree.HTML(r.text)
    last_url = tree.xpath('//div[@class="rbody"]/a[last()-4]/@href')
    return last_url[0]

# 发送post请求下载地图影像


def download_kmz(url):
    formate = '&bboxSR=&layers=&layerDefs=&size=&imageSR=&format=png&transparent=true&dpi=&time=&layerTimeOptions=&dynamicLayers=&gdbVersion=&mapScale=&rotation=&datumTransformations=&layerParameterValues=&mapRangeValues=&layerRangeValues=&f=kmz'
    url = 'http://webmap.iwmi.org' + url + formate
    r = requests.get(url=url, headers=headers)
    dirname = 'kmz'
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    filename_lis = url.split('/')[6:-1]
    filename = "_".join(filename_lis) + '.kmz'
    print('%s正在下载......' % filename)
    filepath = dirname + '/' + filename
    with open(filepath, "wb") as code:
        code.write(r.content)
        print('%s下载完成......' % filename)
        time.sleep(1)


def main():
    url = 'http://webmap.iwmi.org/arcgis/rest/services'
    url_list1 = geturl(url)
    time.sleep(2)
    print('已获取数据链接')
    for url in url_list1:
        url = 'http://webmap.iwmi.org' + url
        try:
            url_list2 = geturl(url)
        except Exception:
            print('下层无更多信息')
        for url in url_list2:
            try:
                url = handel_request(url)
                download_kmz(url)
                time.sleep(1)
            except Exception as e:
                print('发生错误' + str(e))
                time.sleep(5)
    print('已全部下载')


if __name__ == '__main__':
    main()
