import urllib.request
import urllib.parse
import os
url = 'http://tieba.baidu.com/f?ie=utf-8&'

# 需求：输入吧名，输入结束页码然后在当前文件夹创建一个以吧名为文件的文件夹，命名为 吧名_page.html

baname = input('请输入要爬取的吧名')
start_page = int(input('请输入要爬取的开始页码'))
end_page = int(input('请输入要爬取的结束页码'))

# 创建文件夹
if not os.path.exists(baname):
    os.mkdir(baname)

# 搞个循环依次爬取每页数据
for page in range(start_page, end_page + 1):
    # page就是当前页
    # 拼接url的过程
    data = {
        'kw': baname,
        'pn': (page - 1) * 50
    }
    data = urllib.parse.urlencode(data)
    url_t = url + data
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
    }
    request = urllib.request.Request(url=url_t, headers=headers)
    print('第%s页开始下载......' % page)
    response = urllib.request.urlopen(request)

    # 生成文件夹
    filname = baname + '_' + str(page) + '.html'
    # 拼接路径
    filepath = baname + '/' + filname
    with open(filepath, 'wb') as fp:
        fp.write(response.read())
    print('第%s页结束下载......' % page)
