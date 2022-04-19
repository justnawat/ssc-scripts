import pyautogui as pg
from time import sleep
import sys
pg.FAILSAFE = True

pf = sys.platform
if pf == "darwin":
	cmd = "command"
else:
	cmd = "ctrl"

b = 13
e = b + 42
sleep(5)
for i in range(b, e+1):
	# new row + row number
	pg.press("tab")
	pg.write(str(i) + ".")
	pg.press("tab") # doc now in name

	# name
	pg.hotkey("alt", "tab")
	pg.hotkey(cmd, "c")
	pg.press("tab") # response now in id
	pg.hotkey("alt", "tab")
	pg.hotkey(cmd, "v")
	pg.press("tab") # doc now in id

	# id
	pg.hotkey("alt", "tab")
	pg.hotkey(cmd, "c")
	pg.press(["down", "left"]) # response now in next name
	pg.hotkey("alt", "tab")
	pg.hotkey(cmd, "v")
	pg.press("tab") # doc now in pos

	# position
	pg.write("Participant")