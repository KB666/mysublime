import random
print('.......solider.........')
temp = input("猜猜我现在想的是几,只有三次机会呦！")
guess = int(temp)
answer = random.randint(0, 10)
i = 0
while i <= 2:
    if guess > answer:
        temp = input("大了，再猜一次")
        guess = int(temp)
    elif guess < answer:
        temp = input("小了，再猜一次")
        guess = int(temp)
    elif guess == answer:
        print("游戏结束，你赢了。")
        break
    i += 1
    if i >= 3:
        print("游戏结束，你输了。")
print(answer)
