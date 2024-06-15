# 文本输入工具 / Text Input Utility

针对禁用了粘贴功能的各类OJ、写作平台等的PC平台解决方案。

A desktop solution for various OJ and writing platforms that disable paste functionality.

## 实现 / Implementation

使用Python的`pyatuogui`库的`write`函数，模拟键盘输入，做到规避粘贴禁用。

Utilizes Python's `pyautogui` library, specifically the `write` function, to simulate keyboard input, thereby bypassing paste restrictions.

## 使用 / Usage

1. **启动程序：** 运行程序后，弹出带有“开始输入”和“停止输入”选项的窗口，并保持在屏幕前端。

   Upon running, a control window with options "开始输入" and "停止输入" is displayed and remains on top.

2. **文本准备：** 在程序所在目录下准备一个名为`text.txt`的文件，存放待输入的内容。

   Prepare the content to be entered in a file named `text.txt` located in the same directory as the application.

3. **启动输入流程：** 点击“开始输入”，在预设等待时间内（由代码中的`wait`变量决定），鼠标选取输入框位置。

   Initiate the input process by clicking "开始输入", followed by  selecting the input field within the predetermined wait time set by the `wait` variable.

4. **开始输入：** 文本随即开始自动输入。若要中止，可随时按下“停止输入”。

   The text will then be automatically typed. To terminate the input prematurely, press "Stop Input."

5. **连续输入：** 修改`text.txt`文件内容后，无需重启程序，即可为下一轮输入做准备。

   For subsequent rounds of input, simply update the `text.txt` file; no need to restart the application.

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

**v3 **:

* **窗口操控与增强：** 新增控制窗口，且窗口始终保持在最前端，提升用户体验。Add a control window and keep it at the forefront to improve user experience.
* **中途停止支持：** 用户现在可以中途暂停输入过程。 Supports pausing the input process midway through execution.
* **动态内容更新：**  允许修改`text.txt`文件后，无需重启程序即可重新输入新内容。 Enhanced to allow for re-inputting new content after modifying the `text.txt` file without needing to restart the application.

v2 :

* **优化自动补全处理：** 针对输入区域可能出现的自动Tab补全现象进行了改进。 Improved handling to address potential auto-complete suggestions in the input area.

  > 现在，每次模拟输入换行后，程序会先模拟按下`Home`键回到当前行的开头，以避免触发不必要的自动补全建议。
  >
  > After each simulated line break, the program now simulates pressing the `Home` key to return to the beginning of the line, preventing unwanted auto-completion suggestions.
