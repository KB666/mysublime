#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-11 16:50:05
# @Author  : ljljlhj (ljljlhj@foxmail.com)
# @Link    : ${link}
# @Version : $Id$

import pytesseract
from PIL import Image

img = Image.open('code.png')
img = img.convert('RGB')
img = img.convert('L')

print(pytesseract.image_to_string(img))
