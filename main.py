import pyautogui as pg
import time as tm
import re
from tkinter import Tk, Label, Button, Entry, StringVar, END

# 设置启动后等待时间和输入间隔
wait = 2
pause = 0


def start_input():
    global run
    run = True

    start_button.config(state='disabled')  # 禁用开始按钮
    tm.sleep(wait)
    with open("./text.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            if run == False:
                break
            line_text = re.sub(r'[\r\n]+$', '', line)
            pg.press('home')
            pg.write(line_text + "\n", pause)
    run = False
    start_button.config(state='normal')  # 完成后启用开始按钮

def stop_input():
    global run
    run = False

run = False

root = Tk()
root.title("自动化输入控制")
root.attributes('-topmost', True)

Label(root, text=f"请按下开始输入，然后在{wait}s内选中文本框\n\
      如果要中断，可以按下停止输入（有延迟）").pack()

# 开始输入按钮
start_button = Button(root, text="开始输入", command=start_input)
start_button.pack()

# 停止输入按钮
stop_button = Button(root, text="停止输入", command=stop_input, state='normal')
stop_button.pack()

# 主循环
def update_countdown():
    if run and wait > 0:
        wait -= 1
        root.after(1000, update_countdown)  # 每秒更新一次
    

root.after(0, update_countdown)  # 启动倒计时更新
root.mainloop()
