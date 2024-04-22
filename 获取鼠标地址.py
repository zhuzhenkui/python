
# import pyautogui as pag
# import time
# while True:
#     x,y=1886,1000
# # h,w=pag.size()
# #   x,y=pag.position()
#     pag.moveTo(x,y)
#     #
#     time.sleep(1)
#     pag.click()

# import re
# with open('example.txt', 'r') as file:
#     content = file.read().lower()
# words = re.findall(r'\b\w+\b', content)
#
# map_reduces = {}
# for word in words:
#     map_reduces[word] = map_reduces.get(word, 0) + 1
# for word, count in map_reduces.items():
#     print(f'{word}: {count}')

# 模拟键盘输入
from prompt_toolkit.clipboard import pyperclip

point =(100,100)
Flag = 1
pyperclip.copy("Hello, world!")
k.press_key(k.ctrl_l)
k.press_key('v')
k.release_key(k.ctrl_l)
