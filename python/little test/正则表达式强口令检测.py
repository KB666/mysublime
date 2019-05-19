#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-28 21:37:10
# @Author  : ljljlhj (ljljlhj@foxmail.com)
# @Link    : ${link}
# @Version : $Id$

'''
8个以上字符
包含数字
大小写字母
'''

import re


def Examine(Password):
    if len(Password) < 8:
        return False

    regex1 = re.compile(r'[a-z]+')
    regex2 = re.compile(r'[A-Z]+')
    regex3 = re.compile(r'\d+')
    if regex1.search(Password) is None:
        return False
    elif regex2.search(Password) is None:
        return False
    elif regex3.search(Password) is None:
        return False
    else:
        return True


def main():
    Password = input('请输入你的密码：')
    count = 1
    while(count <= 3):
        if Examine(Password):
            print("密码%s满足要求，密码设置成功！" % Password)
            break
        else:
            print("密码不满足要求，至少8个字符且包含大小字母和数字，请重新输入")
            Password = input("请输入要设置的密码：")
        count += 1
    if count > 3:
        print("已经超过最大尝试次数3次，程序退出！")


if __name__ == '__main__':
    main()
