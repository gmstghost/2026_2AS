import time
import pyautogui as gui
import pyperclip as clip

gui.FAILSAFE = True   # 마우스를 화면 모서리로 밀면 중단
gui.PAUSE = 0.5       # 모든 동작 사이에 0.5초 쉬기

print('화면 크기:', gui.size())
print('3초 뒤 시작합니다. 마우스와 키보드에서 손을 떼세요!')
time.sleep(3)

# 윈도우 키 + R -> 실행 창 -> notepad 입력 -> 엔터
gui.hotkey('win', 'r')
gui.write('notepad')
gui.press('enter')
time.sleep(1.5)             # 메모장이 열릴 때까지 기다림

# 한글은 클립보드로 붙여넣기
message = '안녕하세요! 저는 파이썬 로봇입니다.'
clip.copy(message)
gui.hotkey('ctrl', 'v')
gui.press('enter')

clip.copy('이 글은 파이썬이 혼자 썼습니다.')
gui.hotkey('ctrl', 'v')