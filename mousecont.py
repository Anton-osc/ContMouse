import pyautogui as p
from random import randint
p.FAILSAFE = False

while True:
	a = randint(1, 1920)
	b = randint(1, 1000)
	c = randint(1, 1920)
	d = randint(1, 1000)
	p.moveTo(a, b, 0.5)
	p.moveTo(c, d, 0.5)

