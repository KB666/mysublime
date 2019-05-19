#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-02 15:06:02
# @Author  : ljljlhj (ljljlhj@foxmail.com)
# @Link    : ${link}
# @Version : $Id$

import urllib.request
import urllib.parse
import time
import json
import re
"""
接口
https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv35034&productId=7652139&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&rid=0&fold=1"""

item_list = []


def handle_request(url, page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
    }
    url = url % page
    request = urllib.request.Request(url=url, headers=headers)
    return request


def parse(content):
        # 用正则表达式将获取到的内容截取为标准的json格式
    pattern = re.compile(r'fetchJSON_comment98vv35034\((.*?)\);')
    # 将json格式转化为python对象
    ret = pattern.findall(content)[0]
    obj = json.loads(ret)
    # 获取用户名，评论内容，评论时间，商品型号
    # 首先取出comments这个列表
    comments_list = obj['comments']
    # 遍历列表，依次取得每次评论
    for comment in comments_list:
        # 用户名
        name = comment['nickname']
        # 评论内容
        ping_content = comment['content']
        # 评论时间
        ping_time = comment['creationTime']
        # 商品型号
        # 配件
        info = comment['productColor'] + ' ' + comment['productSize'] + \
            ' ' + comment['productSales'][0]['saleValue']
        # 打分
        score = comment['score']
        # 用户等级
        level = comment['userLevelName']
        # 将评论信息保存到字典中
        item = {
            '用户名': name,
            '用户等级': level,
            '打分': score,
            '商品型号': info,
            '评论内容': ping_content,
            '评论时间': ping_time,
        }
        # print(item)
        item_list.append(item)


def main():
    url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv35034&productId=7652139&score=0&sortType=5&page=%s&pageSize=10&isShadowSku=0&rid=0&fold=1'
    start_page = int(input('请输入起始页码:'))
    end_page = int(input('请输入结束页码:'))
    for page in range(start_page - 1, end_page):
        print('第%s页开始爬取..........' % str(page+1))
        request = handle_request(url, page)
        content = urllib.request.urlopen(
            request).read().decode('gbk')
        parse(content)
        print('第%s页爬取成功..........' % str(page+1))
        time.sleep(3)


if __name__ == '__main__':
    main()

    string = json.dumps(item_list, ensure_ascii=False)
    # 保存到文件里
    with open('ping.text', 'w', encoding='utf8')as fp:
        fp.write(string)
