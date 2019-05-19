#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-12 12:44:32
# @Author  : ljljlhj (ljljlhj@foxmail.com)
# @Link    : ${link}
# @Version : $Id$


import time
import threading
'''
不使用线程操作的情况
def sing():
    for x in range(1, 10):
        print('ccccccc')
        time.sleep(1)


def dance():
    for x in range(1, 10):
        print('ttttttt')
        time.sleep(1)


def main():
    sing()
    dance()


if __name__ == '__main__':
    main()
'''

'''
面向对象
def sing(a):
    for x in range(1, int(a)):
        print('ccccccc')
        time.sleep(1)


def dance(a):
    for x in range(1, int(a)):
        print('ttttttt')
        time.sleep(1)


def main():
    a = '6'
    # 创建唱歌线程
    tsing = threading.Thread(target=sing, name="唱歌", args=(a,))
    # 创建跳舞线程
    tdance = threading.Thread(target=dance, name="唱歌", args=(a,))
    tsing.start()
    tdance.start()
    print('主线程')


if __name__ == '__main__':
    main()
'''

# 写一个类，继承自threading.Thread


class SingThread(threading.Thread):
    """docstring for SingThread"""

    def __init__(self, name, a):
        super().__init__()
        self.name = name
        self.a = a

    def run(self):
        for x in range(1, int(self.a)):
            print('cccccc%s' % self.name)
            time.sleep(1)


class DanceThread(threading.Thread):
    """docstring for SingThread"""

    def __init__(self, name, a):
        super().__init__()
        self.name = name
        self.a = a

    def run(self):
        for x in range(1, int(self.a)):
            print('ttttt%s' % self.name)
            time.sleep(1)


def main():
    # 创建线程
    tsing = SingThread('sing', '6')
    tdance = DanceThread('dance', '6')

    # 启动线程
    tsing.start()
    tdance.start()

    # 让主线程等待结束
    tsing.join()
    tdance.join()

    print('主线程')


if __name__ == '__main__':
    main()
