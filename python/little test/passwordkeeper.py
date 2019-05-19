#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-24 14:07:18
# @Author  : ljljlhj (ljljlhj@foxmail.com)
# @Link    : ${link}
# @Version : $Id$

# 书上项目
PASSWORDS = {'emial': '***********', ' blog ': '********'}


import sys
import pyperclip
if len(sys.argv) < 2:
    print(r'usage : python passwordkeeper.py [account] --copy count password')
    sys.exit()

account = sys.argv[1]  # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('password for ' + account + ' is copied tp clipboard.')
else:
    print('there is no account named ' + account)
