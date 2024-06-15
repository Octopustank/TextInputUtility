# 文本输入工具 / Text Input Utility

针对禁用了粘贴功能的各类OJ、写作平台等的PC平台解决方案。

A desktop solution for various OJ and writing platforms that disable paste functionality.

## 实现 / Implementation

使用Python的`pyatuogui`库的`write`函数，模拟键盘输入，做到规避粘贴禁用。

Utilizes Python's `pyautogui` library, specifically the `write` function, to simulate keyboard input, thereby bypassing paste restrictions.

## 使用 / Usage

1. **准备文本：** 文本需放在同目录下的`text.txt`中

   **Prepare Text:** Place your text in a file named `text.txt` within the same directory as the script.

2. **启动：** 启动后，弹出空白窗口。

   **Launch:** Upon starting the utility, a blank window will appear.

3. **选中输入区域：** 关闭窗口后，在设定好的等待时间（代码中`wait`变量的值）内，鼠标选中输入区域

   **Select Input Field:** After closing the window, within the predefined waiting period (set by the `wait` variable in the code), position your cursor to select the target input field.

4. **自动输入：** 随后开始输入

   **Commence Input:** The text will then be automatically typed in.

## 可设置参数 / Configurable Parameters

```python
wait = 2	# 关闭阻滞用窗口后的等待时间
			# Time delay after closing the blocking window before initiating input

pause = 0	# 输入间隔
			# Interval between each character input
```

## 部署 / setup

```shell
pip install -r requirements.txt
```

## 更新日志 / What's New

* **优化自动补全处理：** 针对输入区域可能出现的自动Tab补全现象进行了改进。 Improved handling to address potential auto-complete suggestions in the input area.

  > 现在，每次模拟输入换行后，程序会先模拟按下`Home`键回到当前行的开头，以避免触发不必要的自动补全建议。
  >
  > After each simulated line break, the program now simulates pressing the `Home` key to return to the beginning of the line, preventing unwanted auto-completion suggestions.
