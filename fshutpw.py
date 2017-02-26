#!/usr/bin/env python
# -*- coding:utf-8 -*

from FGPIO.rpiduino_io import *
from FGPIO.bt_io import *
import os

pc = rpiduino_io()
bt = bt_io(pc.bcm_pin(5))

def stop():
	if bt.th_readed():
		bt.stop()
		os.system("shutdown now -h")

def reboot():
	if bt.th_readed():
		bt.stop()
		os.system("reboot")
		

bt.add_thread(reboot) #Si on veut faire un bouton Halt : remplacer "reboot" par "stop"

try: #Ca permet de pouvoir planter le thread avec un CTRL-C
	while True:
		time.sleep(0.1)
except KeyboardInterrupt:
	bt.stop()