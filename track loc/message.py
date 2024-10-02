import pyautogui as p
import time

time.sleep(4)

for i in range(50):
    p.typewrite("HII")
    time.sleep(1)
    p.press("enter")