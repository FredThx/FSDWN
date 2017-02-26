# FSDWN

A small python script to reboot a raspberry pi when a button is presed.

Dependencies :
------------

https://pypi.python.org/pypi/FGPIO/0.6.3

Usage :
-------

Plug a button on GND and GPIO5
Copy the files in /opt/FSDWN
run command : sudo systemctl enable /opt/FSDWN/fshutpw.service
press the button : the raspberry pi reboot

Tutorials :
---------
http://ouiaremakers.com/posts/tutoriel-diy-un-bouton-pour-rebooter-son-raspberry-pi
