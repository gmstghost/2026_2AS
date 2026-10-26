import time
import pyautogui as gui

print('3초 뒤 시작합니다. 메모장을 클릭해 두세요!')
time.sleep(3)

gui.write('hello python')
gui.press('enter')
gui.write('this is my first robot')