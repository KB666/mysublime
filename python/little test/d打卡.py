# 签到打卡升级版
"""author adminster
 2018  05  02
 qq:3315999133"""
import time
f = open('打卡.txt', 'a+')
while True:
    序号 = input("请输入序号，输入零停止")
    if 序号 == "0":
        break
    信息 = 序号 + "号" + time.asctime()
    print(信息 + "打卡")
    f.write(信息 + "\n")
f.close()
