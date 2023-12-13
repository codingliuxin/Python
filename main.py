# 导入模块
import random

# 定义函数
def guess_number():
    number = random.randint(1, 100)
    print("猜猜这个数是多少？")
    while True:
        guess = int(input("请输入你的猜测："))
        if guess == number:
            print("恭喜，猜对了！")
            break
        elif guess < number:
            print("猜小了，请继续猜！")
        else:
            print("猜大了，请继续猜！")

# 主程序
if __name__ == "__main__":
    guess_number()
