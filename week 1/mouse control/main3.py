import pyautogui
import time

pyautogui.moveTo(380, 380)
pyautogui.doubleClick(380, 380)
pyautogui.hotkey('command','a')
pyautogui.hotkey('command','c')
pyautogui.press('backspace')


pyautogui.write('hippety hoppety youre code is now my property')
time.sleep(3)
pyautogui.hotkey('command', 'a')
pyautogui.press('backspace')
pyautogui.hotkey('command', 'v')
