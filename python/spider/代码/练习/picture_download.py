import urllib.request

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
}
image_url = ''
request = urllib.request.Request(url=image_url, headers=headers)
response = urllib.request.urlopen(request)
with open('1.jpg', 'wb') as fp:
    fp.write(response.read())
