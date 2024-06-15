import pyautogui as pg
import time as tm
import re
from tkinter import *

wait = 2 # 启动后等待时间
pause = 0 # 输入间隔

Tk().mainloop() # 阻滞进程，在准备好之后开始输入
tm.sleep(wait)

with open("./text.txt", "r", encoding="utf-8") as f:
    for line in f.readlines():
        line_text = re.sub(r'[\r\n]+$', '', line)
        pg.press('home')
        pg.write(line_text + "\n", pause)


