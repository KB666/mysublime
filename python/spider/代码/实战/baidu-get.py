import urllib.request
import urllib.parse

word = input("请输入你想要查询的内容")
url = 'http://www.baidu.com/s?'

# 参数写成一个字典
data = {
    'ie': 'utf-8',
    'wd': word,
}

# 拼接url
quary_string = urllib.parse.urlencode(data)
url += quary_string

# 发送请求
response = urllib.request.urlopen(url)

filename = word + '.html'
with open(filename, 'wb')as fp:
    fp.write(response.read())
