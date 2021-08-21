# 控制键盘输入
from pynput.keyboard import Controller as key_cl
# 控制鼠标点击
from pynput.mouse import Button, Controller
import time

# 键盘控制函数
def keyboard_input(string):
    # 控制器就行实例化
    keyboard = key_cl()
    keyboard.type(string)

# 鼠标控制函数
def mouse_click():
    mouse = Controller()
    # 点击按钮
    mouse.press(Button.left)
    # 释放按钮
    mouse.release(Button.left)

# 执行函数
def main(n, s):
    time.sleep(6)
    for i in range(n):
        keyboard_input(s)
        mouse_click()
        time.sleep(0.4)

# 软件启动入口
if __name__ == "__main__":
    Number = input("轰炸次数：")
    Data = input("内容：")
    main(int(Number),Data)
