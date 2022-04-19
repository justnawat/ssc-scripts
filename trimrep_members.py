import pyautogui as pg
import pandas as pd
from time import sleep
pg.FAILSAFE = True

path = input("Path to combined members list: ")
df = pd.read_csv(path)

i = 12
sleep(5)
for _, data in df.iterrows():
	name = data.get("names")
	sid = data.get("ids")
	i += 1

	# adding number
	pg.press("tab")
	pg.write(str(i) + ".")
	pg.press("tab")

	# name, id, pos
	pg.write(name)
	pg.press("tab")
	pg.write(str(sid))
	pg.press("tab")
	pg.write("Member")