import time
import keyboard
from PIL import ImageGrab
from baiduapi1 import BaiduApi


def screenshot():
    if keyboard.wait(hotkey='f1') is None:

        time.sleep(0.2)
        im = ImageGrab.grabclipboard()
        im.save('iamgGrab.png')


if __name__ == '__main__': 
    x = 1
    while x < 10:
        screenshot()

        baidu = BaiduApi()

        text = baidu.picture('iamgGrab.png')
        print(text)
