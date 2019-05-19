from PIL import Image
imgad = input('请输入文件的路径和名称')
img = Image.open(imgad)
out = img.convert('L')
width, height = out.size
out = out.resize((int(width * 0.5), int(height * 0.25)))
asciis = "@%#*!-^. "
texts = ""
width, height = out.size
for row in range(height):
    for col in range(width):
        gray = out.getpixel((col, row))
        texts += asciis[int(gray / 255 * 8)]
    texts += '\n'
with open('C:/Users/DELL/Desktop/pic.txt', 'w') as file:
    file.write(texts)
