#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-10 16:39:00
# @Author  : ljljlhj (ljljlhj@foxmail.com)
# @Link    : ${link}
# @Version : $Id$

# https://www.gushiwen.org/
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134', }


def download_code(s):
    url = 'https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx'
    r = s.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    # 获取图片连接
    image_src = 'http://so.gushiwen.org' + \
        soup.find('img', id="imgCode")['src']
    # print(image_src)
    # 下载图片到本地
    image = s.get(url=image_src,headers =headers)
    with open('code.png', 'wb') as fp:
        fp.write(image.content)
    # 查找表但需要的两个参数
    __VIEWSTATE = soup.find('input', id='__VIEWSTATE')['value']
    __VIEWSTATEGENERATOR = soup.find(
        'input', id='__VIEWSTATEGENERATOR')['value']
    return __VIEWSTATE, __VIEWSTATEGENERATOR


def login(view, viewg,s):
    post_url = 'https://so.gushiwen.org/user/login.aspx?from=http%3a%2f%2fso.gushiwen.org%2fuser%2fcollect.aspx '
    # 提示用户输入验证码
    code = input('请输入验证码')
    formdata = {
        '__VIEWSTATE': view,
        '__VIEWSTATEGENERATOR': viewg,
        'from':    'http://so.gushiwen.org/user/collect.aspx',
        'email':   '1582301125@qq.com',
        'pwd': '888888KB',
        'code':    code,
        'denglu':  '登录',
    }
    r = s.post(url=post_url, headers=headers, data=formdata)
    with open('gushi.html', 'w', encoding='utf8') as fp:
        fp.write(r.text)


def main():
    s = requests.session()
    # 下载验证码到本地
    view, viewg = download_code(s)
    # 发送post请求模拟登陆
    login(view, viewg, s)


if __name__ == '__main__':
    main()
