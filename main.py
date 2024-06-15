import pyautogui as pg
import time as tm
from tkinter import *

wait = 2 # 启动后等待时间

pause = 0 # 输入间隔


with open("./text.txt", "r", encoding="utf-8") as f:
    text = f.read()
Tk().mainloop() # 阻滞进程，在准备好之后开始输入
tm.sleep(wait)
pg.write(text, pause)
