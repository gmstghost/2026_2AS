import pyautogui as gui

gui.moveTo(300, 300, duration=1)   # 1초 동안 (300, 300)으로 이동
gui.moveTo(800, 300, duration=1)   # 오른쪽으로 이동
gui.moveTo(800, 600, duration=1)   # 아래로 이동
gui.click()                         # 지금 위치에서 클릭