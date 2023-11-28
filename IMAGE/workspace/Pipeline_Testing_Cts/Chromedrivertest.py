#! /usr/bin/env python3
import time
from pyautogui import hotkey,click

hotkey('ctrl','alt','t')
time.sleep(1)
hotkey('alt','F10')
time.sleep(3)
click(button='left')
time.sleep(2)