#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-31 20:25:01
# @Author  : ljljlhj (ljljlhj@foxmail.com)
# @Link    : ${link}
# @Version : $Id$

'''
头晕做的不完整
'''
import os
import zipfile


def backupToZip(folder):
    folder = os.path.abspath(folder)

    number = 1
    while True:
        zipfilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipfilename):
            break
        number += 1

    print('Creating %s...' % (zipfilename))
    backupZip = zipfile.ZipFile(zipfilename, 'w')

    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s' % (foldername))
        backupZip.write(foldername)
    for filename in filenames:
        newBase = os.path.basename(folder) + '_'
        if filename.startswith(newBase) and filename.endswith('.zip'):
            continue
        backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done')


def main():
    backupToZip('C:\\Users\\15823\\OneDrive\\桌面\\17jp(1)')


if __name__ == '__main__':
    main()
